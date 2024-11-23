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
def json_testfile_1():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file1.json'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def json_testfile_2():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file2.json'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def yaml_testfile_1():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file1.yaml'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def yaml_testfile_2():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file2.yaml'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def data_4_parse_test():
    dict_one = {}
    dict_two = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
    }
    dict_three = {
        'shots': {'1': 1, '2': 2, '3': 3},
        'jack': 'rabbit',
    }
    expected_one = []
    expected_two = [['follow', [False]],
                    ['host', ['hexlet.io']],
                    ['proxy', ['123.234.53.22']],
                    ['timeout', [50]],
                    ]
    expected_three = [['jack', ['rabbit']],
                      ['shots', [['1', [1]],
                                 ['2', [2]],
                                 ['3', [3]]
                                 ],
                       ],
                      ]
    return ((dict_one, expected_one), (dict_two, expected_two),
            (dict_three, expected_three))
