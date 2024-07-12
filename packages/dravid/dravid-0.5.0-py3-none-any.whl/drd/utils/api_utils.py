import requests
import os
import json
import base64
from typing import Dict, Any, Optional
from ..api.dravid_parser import extract_and_parse_xml
import xml.etree.ElementTree as ET
import click

API_URL = 'https://api.anthropic.com/v1/messages'
MODEL = 'claude-3-5-sonnet-20240620'
MAX_TOKENS = 4000


def get_api_key() -> str:
    api_key = os.getenv('CLAUDE_API_KEY')
    if not api_key:
        raise ValueError("CLAUDE_API_KEY not found in environment variables")
    return api_key


def get_headers(api_key: str) -> Dict[str, str]:
    return {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
        'Anthropic-Version': '2023-06-01'
    }


def make_api_call(data: Dict[str, Any], headers: Dict[str, str], stream: bool = False) -> requests.Response:
    response = requests.post(
        API_URL, json=data, headers=headers, stream=stream)
    response.raise_for_status()
    return response


def parse_response(response: str) -> str:
    try:
        root = extract_and_parse_xml(response)
        return ET.tostring(root, encoding='unicode')
    except Exception as e:
        click.echo(f"Error parsing XML response: {e}", err=True)
        return response


def call_dravid_api(query: str, include_context: bool = False, instruction_prompt: Optional[str] = None) -> str:
    api_key = get_api_key()
    headers = get_headers(api_key)

    data = {
        'model': MODEL,
        'system': instruction_prompt or "",
        'messages': [{'role': 'user', 'content': query}],
        'max_tokens': MAX_TOKENS
    }

    response = make_api_call(data, headers)
    resp = response.json()['content'][0]['text']
    # click.echo(f"Raw response from Claude API: {resp}", err=True)

    return parse_response(resp)


def call_dravid_vision_api(query: str, image_path: str, include_context: bool = False, instruction_prompt: Optional[str] = None) -> str:
    api_key = get_api_key()
    headers = get_headers(api_key)

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    data = {
        'model': MODEL,
        'system': instruction_prompt or "",
        'messages': [
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'image',
                        'source': {
                            'type': 'base64',
                            'media_type': 'image/png',
                            'data': image_data
                        }
                    },
                    {
                        'type': 'text',
                        'text': query
                    }
                ]
            }
        ],
        'max_tokens': MAX_TOKENS
    }

    response = make_api_call(data, headers)
    resp = response.json()['content'][0]['text']
    # click.echo(f"Raw response from Claude Vision API: {resp}", err=True)

    return parse_response(resp)


def stream_claude_response(query: str, instruction_prompt: Optional[str] = None) -> str:
    api_key = get_api_key()
    headers = get_headers(api_key)
    headers['Accept'] = 'text/event-stream'

    data = {
        'model': MODEL,
        'system': instruction_prompt or "",
        'messages': [{'role': 'user', 'content': query}],
        'max_tokens': MAX_TOKENS,
        'stream': True
    }

    response = make_api_call(data, headers, stream=True)
    full_response = ""

    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data: '):
                data = json.loads(line[6:])
                if data['type'] == 'content_block_delta':
                    chunk = data['delta']['text']
                    full_response += chunk
                    click.echo(chunk, nl=False)
                elif data['type'] == 'message_stop':
                    click.echo()
                    break

    return full_response
