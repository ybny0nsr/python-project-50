from gendiff.app_logic import read_file_contents, compare_dicts


def test_read_file_contents(test_file_1, test_file_2, diffs):
    dict_1 = read_file_contents(test_file_1)
    dict_2 = read_file_contents(test_file_2)
    result = compare_dicts(dict_1, dict_2)
    assert result == diffs
'{\n    follow: false\n    host: hexlet.io\n    proxy: 123.234.53.22\n    timeout: 50\n}'\
'{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
