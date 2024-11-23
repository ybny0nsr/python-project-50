from gendiff.parsing import parse_n_sort


def test_parse_n_sort(data_4_parse_test):
    for dict, result in data_4_parse_test:
        assert parse_n_sort(dict) == result
