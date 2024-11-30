from gendiff.parsing import adjust_output, get_case, get_key, is_scalar, \
    new_data, original_data


def stylish(diff_rep: list, level=1) -> str:
    INDENT_PER_LEVEL = 4
    PREFIX_WIDTH = 2
    PREFIX_EQUAL = '  '
    PREFIX_ADDED = '+ '
    PREFIX_DELETED = '- '
    PARENTHESIS_OPND = '{'
    PARENTHESIS_CLSD = '}'

    prefix = {'equal values': [PREFIX_EQUAL],
              'added key': [PREFIX_ADDED],
              'missing key': [PREFIX_DELETED],
              'different values': [PREFIX_DELETED, PREFIX_ADDED]}

    get_data_func = {'equal values': [original_data], 'added key': [new_data],
                     'missing key': [original_data],
                     'different values': [original_data, new_data]}
    diff_view = f'{PARENTHESIS_OPND}\n'
    indent = ' ' * (INDENT_PER_LEVEL * level - PREFIX_WIDTH)

    for item in diff_rep:
        case = get_case(item)
        for prefix_, get_data in zip(prefix[case], get_data_func[case]):
            diff_view += indent + prefix_ + get_key(item) + ': '
            data = get_data(item)
            diff_view += adjust_output(data) if is_scalar(
                data) else stylish(data, level + 1)
            diff_view += '\n'
    diff_view += ' ' * (INDENT_PER_LEVEL * (level - 1)) + f'{PARENTHESIS_CLSD}'
    return diff_view
