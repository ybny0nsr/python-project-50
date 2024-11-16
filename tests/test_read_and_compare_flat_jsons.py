from gendiff.app_logic import read_file_contents, compare_dicts


def test_read_file_contents(test_file_1, test_file_2, diffs):
    dict_1 = read_file_contents(test_file_1)
    dict_2 = read_file_contents(test_file_1)
    result = compare_dicts(dict_1, dict_2)
    assert result == diffs