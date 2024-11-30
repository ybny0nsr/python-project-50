import json
import tests.test_diff_dict_rep as t


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


def get_keys(data: list) -> list:
    return [get_key(item) for item in data]


def all_keys(data1: list, data2: list) -> list:
    return sorted(list(set(get_keys(data1) + get_keys(data2))))


# def build_diff(dict1: dict, dict2: dict) -> list:
#     dict1_keys, dict2_keys = set(dict1.keys()), set(dict2.keys())
#
#     all_keys_sorted = sorted(list((dict1_keys | dict2_keys)))
#
#     missing_keys = list(dict1_keys - dict2_keys)
#     added_keys = list(dict2_keys - dict1_keys)
#     diff_values_keys = [key for key in (dict1_keys & dict2_keys) if
#                         dict1[key] != dict2[key]]
#
#     diff_rep = []
#
#     for key in all_keys_sorted:
#         if key in added_keys:
#             new_data = dict2[key]
#             diff_rep.append([key, [], new_data if is_scalar(new_data)
#                             else build_diff(new_data, new_data)])
#
#         elif key in missing_keys:
#             old_data = dict1[key]
#             diff_rep.append([key, old_data if is_scalar(old_data)
#                             else build_diff(old_data, old_data), []])
#
#         elif key in diff_values_keys:
#             old_data = dict1[key]
#             new_data = dict2[key]
#             if is_scalar(old_data) and is_scalar(new_data):
#                 diff_rep.append([key, old_data, new_data])
#             elif is_scalar(old_data) and not is_scalar(new_data):
#                 diff_rep.append(
#                     [key, old_data, build_diff(new_data, new_data)])
#             elif not is_scalar(old_data) and is_scalar(new_data):
#                 diff_rep.append(
#                     [key, build_diff(old_data, old_data), new_data])
#             else:
#                 diff_rep.append([key, build_diff(old_data, new_data)])
#
#         else:
#             data = dict1[key]
#             diff_rep.append([key, data if is_scalar(data)
#                             else build_diff(data, data)])
#     return diff_rep


def get_representation(key, old_data, new_data):
    """Helper to construct the difference representation for a given key."""
    if is_scalar(old_data) and is_scalar(new_data):
        return [key, old_data, new_data]
    elif is_scalar(old_data):
        return [key, old_data, build_diff(new_data, new_data)]
    elif is_scalar(new_data):
        return [key, build_diff(old_data, old_data), new_data]
    else:
        return [key, build_diff(old_data, new_data)]


def build_diff(dict1: dict, dict2: dict) -> list:
    dict1_keys, dict2_keys = set(dict1.keys()), set(dict2.keys())
    all_keys_sorted = sorted(dict1_keys | dict2_keys)

    diff_rep = []
    for key in all_keys_sorted:
        # Added keys:
        if key in dict2_keys - dict1_keys:
            new_data = dict2[key]
            diff_rep.append([key, [],
                             new_data if is_scalar(new_data) else build_diff(
                                 new_data, new_data)])
        # Missing keys:
        elif key in dict1_keys - dict2_keys:
            old_data = dict1[key]
            diff_rep.append([key,
                             old_data if is_scalar(old_data) else build_diff(
                                 old_data, old_data), []])
        # Differing values for the same keys:
        elif key in dict1_keys & dict2_keys and dict1[key] != dict2[key]:
            old_data, new_data = dict1[key], dict2[key]
            diff_rep.append(get_representation(key, old_data, new_data))
        # Identical values for the same keys:
        else:
            old_data = dict1[key]
            diff_rep.append([key,
                             old_data if is_scalar(old_data) else build_diff(
                                 old_data, old_data)])
    return diff_rep


# def prepare_diff_view(diff_rep: list, level=1) -> str:
#     shift = 4
#     prefix = {'equal values': '  ', 'added key': '+ ', 'missing key': '- '}
#
#     bias = ' ' * (shift * level - 2)
#     diff_view = '{\n'
#
#     def process_item(item, case_prefix: str, data_func):
#         nonlocal diff_view
#         diff_view += bias + case_prefix + get_key(item) + ': '
#         data = data_func(item)
#         return adjust_output(data) if is_scalar(data) else prepare_diff_view(
#             data, level + 1)
#
#     for item in diff_rep:
#         case = get_case(item)
#         match case:
#             case 'equal values':
#                 addition = process_item(item, prefix[case],
#                                         original_data)
#             case 'added key':
#                 addition = process_item(item, prefix[case],
#                                         changed_data)
#             case 'missing key':
#                 addition = process_item(item, prefix[case],
#                                         original_data)
#             case 'different values':
#                 addition = process_item(item, prefix['missing key'],
#                                         original_data)
#                 addition += '\n' + bias + prefix['added key'] + get_key(
#                     item) + ': '
#                 data = changed_data(item)
#                 addition += adjust_output(data) if is_scalar(
#                     data) else prepare_diff_view(data, level + 1)
#
#         diff_view += addition + '\n'
#
#     diff_view += ' ' * (shift * (level - 1)) + '}'
#     return diff_view

def prepare_diff_view(diff_rep: list, level=1) -> str:
    shift = 4
    prefix = {'equal values': '  ', 'added key': '+ ', 'missing key': '- '}

    bias = ' ' * (shift * level - 2)
    diff_view = '{\n'

    def process_item(item, case_prefix: str, data_func):
        nonlocal diff_view
        diff_view += bias + case_prefix + get_key(item) + ': '
        data = data_func(item)
        return adjust_output(data) if is_scalar(data) else prepare_diff_view(
            data, level + 1)

    for item in diff_rep:
        case = get_case(item)
        match case:
            case 'equal values':
                addition = bias + prefix[case] + get_key(item) + ': '
                data = original_data(item)
                addition += adjust_output(data) if is_scalar(data) else prepare_diff_view(data, level + 1)
            case 'added key':
                addition = bias + prefix[case] + get_key(item) + ': '
                data = changed_data(item)
                addition += adjust_output(data) if is_scalar(data) else prepare_diff_view(data, level + 1)
            case 'missing key':
                addition = bias + prefix[case] + get_key(item) + ': '
                data = original_data(item)
                addition += adjust_output(data) if is_scalar(data) else prepare_diff_view(data, level + 1)
            case 'different values':
                addition = bias + prefix['missing key'] + get_key(item) + ': '
                data = original_data(item)
                addition += adjust_output(data) if is_scalar(data) else prepare_diff_view(data, level + 1)

                addition += '\n'

                addition += bias + prefix['added key'] + get_key(item) + ': '
                data = changed_data(item)
                addition += adjust_output(data) if is_scalar(data) else prepare_diff_view(data, level + 1)

        diff_view += addition + '\n'

    diff_view += ' ' * (shift * (level - 1)) + '}'
    return diff_view


# Abstractions for operations on internal representation
def get_key(item: list) -> str:
    return item[0]


def original_data(item: list):
    return item[1]


def changed_data(item: list):
    return item[2]


def no_changes_in(item: list) -> bool:
    if len(item) == 2:
        return True

    return False


def is_empty(element):
    if element == []:
        return True
    return False


def is_scalar(element) -> bool:
    return not isinstance(element, list | tuple | set | dict)


def get_case(item: list) -> str:
    if is_empty(original_data(item)):
        return 'added key'
    if no_changes_in(item):
        return 'equal values'
    elif is_empty(changed_data(item)):
        return 'missing key'
    else:
        return 'different values'


if __name__ == '__main__':
    dict1 = json.loads(t.json_file1)
    dict2 = json.loads(t.json_file2)
    result = build_diff(dict1, dict2)

    print(result)
    print(prepare_diff_view(result))
