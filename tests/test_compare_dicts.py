from gendiff.parsing import build_diff, prepare_diff_view

def test_compare_dicts(dict1, dict2, diffs):
    diff = build_diff(dict1, dict2)
    assert prepare_diff_view(diff) == diffs