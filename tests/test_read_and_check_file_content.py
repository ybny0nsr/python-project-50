from gendiff.parsing import read_file_contents


def test_read_file_contents(json_testfile1, dict1):
    content = read_file_contents(json_testfile1)
    assert content == dict1