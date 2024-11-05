from subprocess import run


resp_one = '''usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help   show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output'''


def test_help():
    result = run(['gendiff', '-h'], capture_output=True, text=True)
    output = result.stderr.rstrip()
    assert output == resp_one
