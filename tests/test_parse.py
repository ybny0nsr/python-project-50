import pytest
from gendiff.parsing import parse_n_sort


dict_one = {}
expected_one = []
dict_two = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False,
}
expected_two = [['follow', [False]],
                ['host', ['hexlet.io']],
                ['proxy', ['123.234.53.22']],
                ['timeout', [50]],
                ]
dict_three = {
    'shots': {'1': 1, '2': 2, '3': 3},
    'jack': 'rabbit',
}
expected_three = [['jack', ['rabbit']],
                  ['shots', [['1', [1]],
                             ['2', [2]],
                             ['3', [3]]
                             ],
                   ],
                  ]


@pytest.mark.parametrize(("data", "expected_result"),
                         [(dict_one, expected_one),
                          (dict_two, expected_two),
                          (dict_three, expected_three),
                          ],
                         )
def test_parse_n_sort(data: dict, expected_result: list) -> None:
    assert parse_n_sort(data) == expected_result
