import json
import os
import yaml
# TODO оставить только нужные импорты

def parse_n_sort(template: dict) -> list:
    result = []
    for key, value in template.items():
        result.append(
            [key, parse_n_sort(value)] if isinstance(value, dict)
            else [key, [value]])
    result.sort()
    return result


def file_not_found(file: str) -> bool:
    return not os.path.isfile(file)


def are_files_missing(*files: str) -> bool:
    at_least_one_is_missing = False
    error_message = ''
    for file in files:
        if file_not_found(file):
            error_message += f"{', ' if at_least_one_is_missing else ''}{file}"
            at_least_one_is_missing = True
    if at_least_one_is_missing:
        print('FileNotFoundError:', error_message)
    return at_least_one_is_missing


def get_file_ext(file: str) -> str:
    return os.path.splitext(file)[-1]


def ext_is_yaml(file: str) -> bool:
    return get_file_ext(file) in ('.yaml', '.yml')


def ext_is_json(file: str) -> bool:
    return get_file_ext(file) == '.json'


def read_file_contents(file: str) -> dict:
    try:
        with open(file, 'r') as f:
            if ext_is_json(file):
                return json.load(f)
            if ext_is_yaml(file):
                return yaml.safe_load(f)
            else:
                print(f'The file {file} has an invalid extension')
    except Exception:
        print(f'An error occurred while reading the file "{file}')
