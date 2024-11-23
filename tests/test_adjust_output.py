import pytest
from gendiff.app_logic import adjust_output


@pytest.mark.parametrize(("python_data", "like_json_view"),
                         [(False, 'false'),
                          (True, 'true'),
                          (None, 'null'),
                          (123, '123'),
                          (1.23, '1.23'),
                          ([1, 'abc', 3.14], "[1, 'abc', 3.14]"),
                          ('hexlet', 'hexlet'),
                          ({"a": 1, "b": 1.0}, "{'a': 1, 'b': 1.0}"),
                          ],
                         )
def test_python_to_json(python_data, like_json_view):
    assert adjust_output(python_data) == like_json_view
