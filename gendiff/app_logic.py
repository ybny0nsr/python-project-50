from sys import exit
from gendiff.file_ops import are_files_missing, read_file_contents
from gendiff.parsing import build_diff, prepare_diff_view


def generate_diff(file_1: str, file_2: str,  format_name='stylish'):
    if are_files_missing(file_1, file_2):
        exit(1)

    dict1 = read_file_contents(file_1)
    dict2 = read_file_contents(file_2)

    if None in (dict1, dict2):
        exit(1)

    diff = build_diff(dict1, dict2)
    print(prepare_diff_view(diff))
