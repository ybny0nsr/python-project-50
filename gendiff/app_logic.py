import json
import os
import sys


def file_not_found(file: str) -> bool:
    return not os.path.isfile(file)


def files_not_found(*files: tuple) -> bool:
    check_status = False
    message = ''
    for file in files:
        if file_not_found(file):
            if not check_status:
                message += 'FileNotFoundError: '
            else:
                message += ', '
            message += f'{file}'
            check_status = True
    print(message)
    return check_status


def read_file_contents(file: str) -> dict:
    try:
        return json.load(open(file))
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


def find_diffs_json(dict_1: dict, dict_2: dict) -> str:
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
            result += f'{offset}- {key}: {dict_1[key]}\n'
            result += f'{offset}+ {key}: {dict_2[key]}\n'
        elif key in diff_plus:
            result += f'{offset}+ {key}: {dict_2[key]}\n'
        elif key in diff_minus:
            result += f'{offset}- {key}: {dict_1[key]}\n'
        else:
            result += f'{offset}  {key}: {dict_1[key]}\n'
    result += '}'
    return result


def generate_diff(file_1: str, file_2: str):
    if files_not_found(file_1, file_2):
        sys.exit(1)

    template_1 = read_file_contents(file_1)
    template_2 = read_file_contents(file_2)
    print(type(template_1))
    if None in (template_1, template_2):
        sys.exit(1)

    list_1 = parse_n_sort(template_1)
    list_2 = parse_n_sort(template_2)

    print(f'{template_1=}\n{list_1=}\n')
    print(f'{template_2=}\n{list_2=}')
