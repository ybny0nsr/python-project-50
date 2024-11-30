def adjust_output(value):
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return f'{value}'


def adapt(data):
    return data if is_scalar(data) else build_diff(data, data)


def build_diff(dict1: dict, dict2: dict) -> list:
    dict1_keys, dict2_keys = set(dict1.keys()), set(dict2.keys())

    all_keys_sorted = sorted(list((dict1_keys | dict2_keys)))
    missing_keys = list(dict1_keys - dict2_keys)
    added_keys = list(dict2_keys - dict1_keys)
    diff_values_keys = [key for key in (dict1_keys & dict2_keys) if
                        dict1[key] != dict2[key]]
    diff_rep = []
    for key in all_keys_sorted:
        if key in added_keys:
            diff_rep.append([key, [], adapt(dict2[key])])
        elif key in missing_keys:
            diff_rep.append([key, adapt(dict1[key]), []])
        elif key in diff_values_keys:
            if not is_scalar(dict1[key]) and not is_scalar(dict2[key]):
                diff_rep.append([key, build_diff(dict1[key], dict2[key])])
            else:
                diff_rep.append([key, adapt(dict1[key]), adapt(dict2[key])])
        else:  # = "key in equal_values_keys"
            data = adapt(dict1[key])
            diff_rep.append([key, data])
    return diff_rep


def prepare_diff_view(diff_rep: list, level=1) -> str:
    indent_per_level = 4
    prefix_width = 2
    prefix = {'equal values': ['  '], 'added key': ['+ '],
              'missing key': ['- '], 'different values': ['- ', '+ ']}
    get_data_func = {'equal values': [original_data], 'added key': [new_data],
                     'missing key': [original_data],
                     'different values': [original_data, new_data]}
    indent = ' ' * (indent_per_level * level - prefix_width)
    diff_view = '{\n'

    for item in diff_rep:
        case = get_case(item)
        for prefix_, get_data in zip(prefix[case], get_data_func[case]):
            diff_view += indent + prefix_ + get_key(item) + ': '
            data = get_data(item)
            diff_view += adjust_output(data) if is_scalar(
                data) else prepare_diff_view(data, level + 1)
            diff_view += '\n'
    diff_view += ' ' * (indent_per_level * (level - 1)) + '}'
    return diff_view


# Abstractions for operations on internal representation
def get_key(item: list) -> str:
    return item[0]


def original_data(item: list):
    return item[1]


def new_data(item: list):
    return item[2]


def no_changes_in(item: list) -> bool:
    if len(item) == 2:
        return True

    return False


def is_void(element):
    if element == []:
        return True
    return False


def is_scalar(element) -> bool:
    return not isinstance(element, list | tuple | set | dict)


def get_case(item: list) -> str:
    if is_void(original_data(item)):
        return 'added key'
    if no_changes_in(item):
        return 'equal values'
    elif is_void(new_data(item)):
        return 'missing key'
    else:
        return 'different values'
