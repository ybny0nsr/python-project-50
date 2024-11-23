from sys import exit
from gendiff.parsing import are_files_missing, read_file_contents


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
    if are_files_missing(file_1, file_2):
        exit(1)

    dict_1 = read_file_contents(file_1)
    dict_2 = read_file_contents(file_2)

    if None in (dict_1, dict_2):
        exit(1)

    # list_1 = parsing.parse_n_sort(dict_1)
    # list_2 = parsing.parse_n_sort(dict_2)
    #
    # print(f'{template_1=}\n{list_1=}\n')
    # print(f'{template_2=}\n{list_2=}')

    print(compare_dicts(dict_1, dict_2))
