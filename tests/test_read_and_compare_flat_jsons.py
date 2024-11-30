from gendiff.file_ops import read_file_contents
from gendiff.parsing import build_diff
from gendiff.formatters import stylish


def test_read_file_contents(json_testfile1, json_testfile2, diffs):
    dict_1 = read_file_contents(json_testfile1)
    dict_2 = read_file_contents(json_testfile2)
    diff = build_diff(dict_1, dict_2)
    result = stylish(diff)
    assert result == diffs
