from gendiff.parsing import are_files_missing
import os


def test_files_not_found():
    assert are_files_missing('fake_filename_1.ext', 'fake_file_name_2.ext')
    assert not are_files_missing(os.path.realpath(__file__), os.path.realpath(__file__))