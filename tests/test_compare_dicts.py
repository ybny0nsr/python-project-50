from gendiff.app_logic import compare_dicts


dict_1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

dict_2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


def test_compare_dicts():
    assert compare_dicts(dict_1, dict_2) == (
        '{\n  - follow: false\n    host: hexlet.io\n  - proxy: '
        '123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: '
        'true\n}')
