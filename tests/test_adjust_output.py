from gendiff.app_logic import adjust_output


def test_python_to_json():
    assert adjust_output(False) == 'false'
    assert adjust_output(True) == 'true'
    assert adjust_output(None) == 'null'
    assert adjust_output(123) == '123'
    assert adjust_output(1.23) == '1.23'
    assert adjust_output([1, 'abc', 3.14]) == "[1, 'abc', 3.14]"
    assert adjust_output("hexlet") == "hexlet"
    assert adjust_output({"a": 1, "b": 1.0}) == "{'a': 1, 'b': 1.0}"