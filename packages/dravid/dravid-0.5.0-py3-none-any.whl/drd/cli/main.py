import click
from dotenv import load_dotenv
from colorama import init
from .commands import dravid_cli_logic

# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

@click.command()
@click.argument('query', required=False)
@click.option('--image', type=click.Path(exists=True), help='Path to an image file to include with the query')
@click.option('--debug', is_flag=True, help='Print more information on how this coding assistant executes your instruction')
@click.option('--monitor-fix', is_flag=True, help='Start the dev server monitor to automatically fix errors')
@click.option('--meta-add', help='Update metadata based on the provided description')
@click.option('--meta-init', is_flag=True, help='Initialize project metadata')
@click.option('--ask', help='Ask an open-ended question and get a streamed response from Claude')
@click.option('--file', type=click.Path(), multiple=True, help='Read content from specified file(s) and include in the context')
def dravid_cli(query, image, debug, monitor_fix, meta_add, meta_init, ask, file):
    dravid_cli_logic(query, image, debug, monitor_fix, meta_add, meta_init, ask, file)

if __name__ == '__main__':
    dravid_cli()