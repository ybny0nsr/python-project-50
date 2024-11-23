from gendiff.app_logic import compare_dicts


def test_compare_dicts(dict1, dict2, diffs):
    assert compare_dicts(dict1, dict2) == diffs