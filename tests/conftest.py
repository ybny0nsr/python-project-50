import pytest
import os.path
import json
import yaml


@pytest.fixture
def dict1():
    test_dict1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    return test_dict1


@pytest.fixture
def dict2():
    test_dict2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
    return test_dict2


@pytest.fixture
def diffs():
    diff = (
        '{\n  - follow: false\n    host: hexlet.io\n  - proxy: '
        '123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: '
        'true\n}')
    return diff


@pytest.fixture()
def json_testfile1():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file1.json'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def json_testfile2():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file2.json'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def json_testdata1():
    json_file = '''{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": true,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}'''
    return json.loads(json_file)


@pytest.fixture()
def json_testdata2():
    json_file = '''{
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}'''
    return json.loads(json_file)


@pytest.fixture()
def yaml_testfile1():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file1.yaml'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def yaml_testfile2():
    current_path = os.path.dirname(__file__)
    file = 'fixtures/flat_file2.yaml'
    file_w_path = os.path.join(current_path, file)
    return file_w_path


@pytest.fixture()
def yaml_testdata1() -> dict:
    yaml_file = '''common:
  setting1: Value 1
  setting2: 200
  setting3: true
  setting6:
    key: value
    doge:
      wow: ''
group1:
  baz: bas
  foo: bar
  nest:
    key: value
group2:
  abc: 12345
  deep:
    id: 45
'''
    return yaml.safe_load(yaml_file)

@pytest.fixture()
def yaml_testdata2() -> dict:
    yaml_file = '''common:
  follow: false
  setting1: Value 1
  setting3: null
  setting4: blah blah
  setting5:
    key5: value5
  setting6:
    key: value
    ops: vops
    doge:
      wow: so much
group1:
  foo: bar
  baz: bars
  nest: str
group3:
  deep:
    id:
      number: 45
  fee: 100500'''
    return yaml.safe_load(yaml_file)
