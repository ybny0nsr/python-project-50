import json
import os
import sys


def file_not_found(file) -> bool:
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


def read_file_contents(file):
    try:
        return json.load(open(file))
    except Exception:
        print(f'An error occurred while reading the file "{file}')


def parse_n_sort(template: dict):
    result = []
    for key, value in template.items():
        result.append(
            [key, parse_n_sort(value)] if isinstance(value, dict)
            else [key, [value]])
    result.sort()
    return result


def engine(args):
    file_1 = args.first_file
    file_2 = args.second_file

    if files_not_found(file_1, file_2):
        sys.exit(1)

    template_1 = read_file_contents(file_1)
    template_2 = read_file_contents(file_2)
    if None in (template_1, template_2):
        sys.exit(1)

    structure_1 = parse(template_1)
    structure_2 = parse(template_2)

    print(f'{template_1=}\n{structure_1=}\n')
    print(f'{template_2=}\n{structure_2=}')