import json
import os
import sys
import yaml
# TODO оставить только нужные импорты


def file_not_found(file: str) -> bool:
    return not os.path.isfile(file)


def files_not_found(*files: str) -> bool:
    file_is_missing = False
    error_message = ''
    for file in files:
        if file_not_found(file):
            error_message += f"{', ' if file_is_missing else ''}{file}"
            file_is_missing = True
    if file_is_missing:
        print('FileNotFoundError:', error_message)
    return file_is_missing


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


def parse_n_sort(template: dict) -> list:
    result = []
    for key, value in template.items():
        result.append(
            [key, parse_n_sort(value)] if isinstance(value, dict)
            else [key, [value]])
    result.sort()
    return result


def adjust_output(value):
    match value:
        case True: return 'true'
        case False: return 'false'
        case None: return 'null'
        case _: return f'{value}'


def compare_dicts(dict_1: dict, dict_2: dict) -> str:
    result = '{\n'
    offset = '  '
    keys_1, keys_2 = set(dict_1.keys()), set(dict_2.keys())
    diff_values = {key for key in keys_1 & keys_2 if
                   dict_1[key] != dict_2[key]}
    diff_plus = keys_2 - keys_1
    diff_minus = keys_1 - keys_2
    keys_list = sorted(list(keys_1 | keys_2))
    for key in keys_list:
        if key in diff_values:
            result += f'{offset}- {key}: ' + adjust_output(dict_1[key]) + '\n'
            result += f'{offset}+ {key}: ' + adjust_output(dict_2[key]) + '\n'
        elif key in diff_plus:
            result += f'{offset}+ {key}: ' + adjust_output(dict_2[key]) + '\n'
        elif key in diff_minus:
            result += f'{offset}- {key}: ' + adjust_output(dict_1[key]) + '\n'
        else:
            result += f'{offset}  {key}: ' + adjust_output(dict_1[key]) + '\n'
    result += '}'
    return result


def generate_diff(file_1: str, file_2: str):
    if files_not_found(file_1, file_2):
        sys.exit(1)

    dict_1 = read_file_contents(file_1)
    dict_2 = read_file_contents(file_2)

    if None in (dict_1, dict_2):
        sys.exit(1)

    # list_1 = parse_n_sort(dict_1)
    # list_2 = parse_n_sort(dict_2)
    #
    # print(f'{template_1=}\n{list_1=}\n')
    # print(f'{template_2=}\n{list_2=}')

    print(compare_dicts(dict_1, dict_2))
