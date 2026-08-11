import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json(file_path):
    if not os.path.exists(file_path):
        logger.error(f'File not found: {file_path}')
        return None
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            logger.info(f'Successfully loaded JSON data from {file_path}')
            return data
        except json.JSONDecodeError:
            logger.error('Failed to decode JSON')
            return None


def save_json(data, file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        logger.info(f'Successfully saved data to {file_path}')


def list_files_in_directory(dir_path):
    try:
        return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    except Exception as e:
        logger.error(f'Error listing files in directory: {e}')
        return []


def get_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lstrip('.')


def truncate_string(string, max_length):
    if len(string) > max_length:
        logger.warning('String truncated from {len(string)} to {max_length}')
        return string[:max_length] + '...'
    return string
