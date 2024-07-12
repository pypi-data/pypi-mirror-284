import click
import time
import re
import os
import traceback
from typing import Dict, Callable
from ..api.dravid_api import call_dravid_api
from ..api.dravid_parser import parse_dravid_response, pretty_print_commands
from ..utils.step_executor import Executor
from ..utils.utils import print_error, print_success, print_info, get_project_context
from ..prompts.error_handling import handle_error_with_dravid
from ..metadata.project_metadata import ProjectMetadataManager
from queue import Queue, Empty
import threading
import subprocess


class DevServerMonitor:
    def __init__(self, project_dir: str, error_handlers: dict):
        self.project_dir = project_dir
        self.metadata_manager = ProjectMetadataManager(project_dir)
        self.error_handlers = error_handlers
        self.process = None
        self.output_queue = Queue()
        self.should_stop = threading.Event()

    def start(self):
        dev_server_info = self.metadata_manager.get_dev_server_info()
        start_command = dev_server_info.get('start_command')
        if not start_command:
            raise ValueError("Dev server start command not found in metadata")

        click.echo(f"Starting dev server with command: {start_command}")
        self.process = subprocess.Popen(
            start_command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
            cwd=self.project_dir
        )
        threading.Thread(target=self._enqueue_output, args=(
            self.process.stdout, self.output_queue), daemon=True).start()
        threading.Thread(target=self._monitor_output, daemon=True).start()

    def _enqueue_output(self, out, queue):
        for line in iter(out.readline, ''):
            queue.put(line)
        out.close()

    def _monitor_output(self):
        while not self.should_stop.is_set():
            try:
                line = self.output_queue.get(timeout=0.1)
                click.echo(line, nl=False)  # Print server output in real-time
                for error_pattern, handler in self.error_handlers.items():
                    if re.search(error_pattern, line, re.IGNORECASE):
                        handler(line, self)
            except Empty:
                continue

    def stop(self):
        self.should_stop.set()
        if self.process:
            self.process.terminate()
            self.process.wait()

    def restart(self):
        print_info("Restarting development server...")
        self.stop()
        print_info("Server stopped. Starting again...")
        self.start()
        print_success("Server restarted successfully.")
        print_info("Waiting for server output...")

        # Wait for some initial output after restart
        timeout = 10  # seconds
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                line = self.output_queue.get(timeout=0.5)
                print(line, end='')
                if "started" in line.lower() or "listening" in line.lower():
                    print_success("Server is up and running!")
                    break
            except Empty:
                pass
        else:
            print_success(
                "Timeout waiting for server startup message. It may still be starting...")

        print_info("Continuing to monitor server output. Press Ctrl+C to stop.")


def run_dev_server_with_monitoring():
    print_info("Starting dev server monitor...")
    error_handlers = {
        r"(?:Cannot find module|Module not found|ImportError|No module named)": handle_module_not_found,
        r"SyntaxError": handle_syntax_error,
        r"(?:EADDRINUSE|address already in use)": handle_port_in_use,
    }
    current_dir = os.getcwd()
    monitor = DevServerMonitor(current_dir, error_handlers)
    try:
        monitor.start()
        print_info("Dev server monitor started. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print_info("Stopping development server...")
    finally:
        monitor.stop()


def handle_module_not_found(line, monitor):
    match = re.search(
        r"(?:Cannot find module|Module not found|ImportError|No module named).*['\"](.*?)['\"]", line, re.IGNORECASE)
    if match:
        module_name = match.group(1)
        error = ImportError(f"Module '{module_name}' not found")
        monitoring_handle_error_with_dravid(error, line, monitor)


def handle_syntax_error(line, monitor):
    error = SyntaxError(f"Syntax error in line: {line}")
    monitoring_handle_error_with_dravid(error, line, monitor)


def handle_port_in_use(line, monitor):
    match = re.search(
        r"(?:EADDRINUSE|address already in use).*:(\d+)", line, re.IGNORECASE)
    if match:
        port = match.group(1)
        error = OSError(f"Port {port} is already in use")
        monitoring_handle_error_with_dravid(error, line, monitor)


def monitoring_handle_error_with_dravid(error, line, monitor):
    print_error(f"Error detected: {error}")

    error_message = str(error)
    error_type = type(error).__name__
    error_trace = ''.join(traceback.format_exception(
        type(error), error, error.__traceback__))
    project_context = monitor.metadata_manager.get_project_context()

    error_query = f"""
# Error Context
An error occurred while running the dev server:

Error type: {error_type}
Error message: {error_message}

Error trace:
{error_trace}

Relevant output line:
{line}

Project context:
{project_context}

# Instructions for dravid: Error Resolution Assistant
Analyze the error above and provide steps to fix it.
This is being run in a monitoring thread, so don't suggest server starting commands like npm run dev.
Your response should be in strictly XML format with no other extra messages. Use the following format:
<response>
<explanation>A brief explanation of the steps, if necessary</explanation>
<steps>
    <step>
    <type>shell</type>
    <command>command to execute</command>
    </step>
    <step>
    <type>file</type>
    <operation>CREATE</operation>
    <filename>path/to/file.ext</filename>
    <content>
        <![CDATA[
        file content here
        ]]>
    </content>
    </step>
    <step>
    <type>file</type>
    <operation>UPDATE</operation>
    <filename>path/to/existing/file.ext</filename>
    <content>
        <![CDATA[
        content to append or replace
        ]]>
    </content>
    </step>
    <step>
    <type>file</type>
    <operation>DELETE</operation>
    <filename>path/to/file/to/delete.ext</filename>
    </step>
</steps>
</response>
"""

    print_info("Sending error information to Dravid for analysis...")
    response = call_dravid_api(error_query, include_context=True)

    try:
        fix_commands = parse_dravid_response(response)
    except ValueError as e:
        print_error(f"Error parsing dravid's response: {str(e)}")
        return False

    print_info("dravid's suggested fix:")
    pretty_print_commands(fix_commands)

    if click.confirm("Do you want to apply this fix?"):
        print_info("Applying dravid's suggested fix...")
        executor = Executor()
        for cmd in fix_commands:
            if cmd['type'] == 'shell':
                print_info(f"Executing: {cmd['command']}")
                executor.execute_shell_command(cmd['command'])
            elif cmd['type'] == 'file':
                print_info(
                    f"Performing file operation: {cmd['operation']} on {cmd['filename']}")
                executor.perform_file_operation(
                    cmd['operation'], cmd['filename'], cmd.get('content'))
        print_success("Fix applied. Restarting server...")
        monitor.restart()
        return True
    else:
        print_info("Fix not applied. Continuing with current state.")
        return False
