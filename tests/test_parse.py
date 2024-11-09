from gendiff.app_logic import parse


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



def test_parse():
    assert parse(structure_1) == []
    assert parse(structure_2) == [['host', ['hexlet.io']],
                                  ['timeout', [50]],
                                  ['proxy', ['123.234.53.22']],
                                  ['follow', [False]],
                                  ]
    assert parse(structure_3) == [['shots', [['1', [1]],
                                             ['2', [2]],
                                             ['3', [3]]
                                             ],
                                   ],
                                   ['jack', ['rabbit']],
                                  ]
