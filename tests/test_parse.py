from gendiff.app_logic import parse_n_sort


structure_1 = {}
structure_2 = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False,
}
structure_3 = {
    'shots': {'1': 1, '2': 2, '3': 3},
    'jack': 'rabbit',
}



def test_parse_n_sort():
    assert parse_n_sort(structure_1) == []
    assert parse_n_sort(structure_2) == [['follow', [False]],
                                  ['host', ['hexlet.io']],
                                  ['proxy', ['123.234.53.22']],
                                  ['timeout', [50]],
                                  ]
    assert parse_n_sort(structure_3) == [['jack', ['rabbit']],
                                   ['shots', [
                                             ['1', [1]],
                                             ['2', [2]],
                                             ['3', [3]]
                                             ],
                                   ],
                                  ]
