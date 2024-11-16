import pytest
import os.path


@pytest.fixture
def dict_1():
    test_dict_1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}
    return test_dict_1


@pytest.fixture
def dict_2():
    test_dict_2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}
    return test_dict_2


@pytest.fixture
def diffs():
    diff = (
        '{\n  - follow: false\n    host: hexlet.io\n  - proxy: '
        '123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: '
        'true\n}')
    return diff

@pytest.fixture()
def test_file_1():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file_1.json'
    file_w_path = os.path.join(current_path, file)
    return file_w_path

@pytest.fixture()
def test_file_2():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file_2.json'
    file_w_path = os.path.join(current_path, file)
    return file_w_path