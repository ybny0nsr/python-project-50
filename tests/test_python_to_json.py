from gendiff.app_logic import python_to_json


def test_python_to_json():
    assert python_to_json(False) == 'false'
    assert python_to_json(True) == 'true'
    assert python_to_json(None) == 'null'
    assert python_to_json(123) == '123'
    assert python_to_json(1.23) == '1.23'
    assert python_to_json([1, 'abc', 3.14]) == "[1, 'abc', 3.14]"
    assert python_to_json("hexlet") == "hexlet"
    assert python_to_json({"a": 1, "b": 1.0}) == "{'a': 1, 'b': 1.0}"