from gendiff.app_logic import read_file_contents, compare_dicts


def test_read_file_contents(json_testfile_1, json_testfile_2, diffs):
    dict_1 = read_file_contents(json_testfile_1)
    dict_2 = read_file_contents(json_testfile_2)
    result = compare_dicts(dict_1, dict_2)
    assert result == diffs
