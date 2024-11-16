from gendiff.app_logic import compare_dicts


def test_compare_dicts(dict_1, dict_2, diffs):
    assert compare_dicts(dict_1, dict_2) == diffs