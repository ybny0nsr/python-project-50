import yaml

import gendiff.formatters
import gendiff.parsing as d


def test_diff_jsons(yaml_testdata1, yaml_testdata2, diff_testdata):
    dict1 = yaml.safe_load(yaml_testdata1)
    dict2 = yaml.safe_load(yaml_testdata2)
    result = d.build_diff(dict1, dict2)
    assert gendiff.formatters.stylish(result) == diff_testdata