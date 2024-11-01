def input_to_int_list(split_str=" "):
    """
    输入转list
    :param split_str: 分割的字符
    :return:
    """
    return list(map(int, input().split(split_str)))


def input_to_one_int():
    return int(input())


def input_to_more_int(split_str = " "):
    return map(int, input().split(split_str))
