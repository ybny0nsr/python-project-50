from gendiff.file_ops import read_file_contents
from gendiff.parsing import build_diff, prepare_diff_view


def test_read_file_contents(yaml_testfile1, yaml_testfile2, diffs):
    dict_1 = read_file_contents(yaml_testfile1)
    dict_2 = read_file_contents(yaml_testfile2)
    result = prepare_diff_view(build_diff(dict_1, dict_2))
    assert result == diffs
