from subprocess import run


resp_one = '''usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output\n'''


def test_help(capsys):
    result = run(['gendiff', '-h'], capture_output=True, text=True)
    assert result.stdout == resp_one


