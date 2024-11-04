from subprocess import run


resp_one = '''usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help   show this help message and exit'''


resp_two = '''usage: gendiff [-h] first_file second_file
gendiff: error: the following arguments are required: first_file, second_file'''


def test_help():
    result = run(['gendiff', '-h'], capture_output=True, text=True)
    output = result.stdout.rstrip()
    assert output == resp_one
