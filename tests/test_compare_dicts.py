from gendiff.parsing import build_diff
from gendiff.formatters import stylish


def test_compare_dicts(dict1, dict2, diffs):
    diff = build_diff(dict1, dict2)
    assert stylish(diff) == diffs