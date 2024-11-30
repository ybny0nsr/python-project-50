import json

import gendiff.formatters
import gendiff.parsing as d


def test_diff_jsons(json_testdata1, json_testdata2, diff_testdata):
    dict1 = json.loads(json_testdata1)
    dict2 = json.loads(json_testdata2)
    result = d.build_diff(dict1, dict2)
    assert gendiff.formatters.stylish(result) == diff_testdata