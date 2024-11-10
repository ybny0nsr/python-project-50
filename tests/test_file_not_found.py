from gendiff.app_logic import file_not_found
import os


def test_file_not_found():
    assert file_not_found('fake_file_name.ext')
    assert not file_not_found(os.path.realpath(__file__))