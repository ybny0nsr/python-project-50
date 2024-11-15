from gendiff.app_logic import files_not_found
import os


def test_files_not_found():
    assert files_not_found('fake_filename_1.ext','fake_file_name_2.ext')
    assert not files_not_found(os.path.realpath(__file__), os.path.realpath(__file__))