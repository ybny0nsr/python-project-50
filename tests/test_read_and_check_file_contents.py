from gendiff.app_logic import read_file_contents


def test_read_file_contents(test_file_1, dict_1):
    read_content = read_file_contents(test_file_1)
    assert read_content == dict_1