from gendiff.app_logic import read_file_contents


def test_read_file_contents(json_testfile_1, dict_1):
    content = read_file_contents(json_testfile_1)
    assert content == dict_1