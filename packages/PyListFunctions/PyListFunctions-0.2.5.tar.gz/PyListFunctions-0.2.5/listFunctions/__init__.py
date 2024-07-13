# Author: BL_30G
# Version: 0.2

def tidy_up_list(lst: list, bool_mode: bool = False, eval_mode: bool = False) -> list:
    """
    A function to tidy up list(●ˇ∀ˇ●)

    :param bool_mode: If you want to turn such as 'True' into True which it is in this list, you can turn on 'bool_mode' (～￣▽￣)～
    :param eval_mode: If you want to turn such as '[]' into [] which it is in this list, you can turn on 'eval_mode' (￣◡￣)
    :param lst:put list which you need to sorting and clean（￣︶￣）
    :return: the perfect list  ( ´◡` )

    """

    # 判断是否是list类型，否则返回形参原本值
    if type(lst) is not list:
        return lst

    _lst_types: list = []
    _point_j: int = 0
    _point_l: list = []
    _str_app_l: list = []
    _spe_type_content: dict = {'lst': [], 'dic': [], 'set': [], 'tuple': [], 'complex': []}

    # 保存原有特殊变量原本值
    for i in range(len(lst)):
        if type(lst[i]) is list:
            if lst[i] not in _spe_type_content['lst']:
                _spe_type_content['lst'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is dict:
            if lst[i] not in _spe_type_content['dic']:
                _spe_type_content['dic'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is set:
            if lst[i] not in _spe_type_content['set']:
                _spe_type_content['set'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is tuple:
            if lst[i] not in _spe_type_content['tuple']:
                _spe_type_content['tuple'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is complex:
            if lst[i] not in _spe_type_content['complex']:
                _spe_type_content['complex'].append(lst[i])
            lst[i] = str(lst[i])

    # 排序+去除重复值
    lst = set(lst)
    lst = list(lst)
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    lst = sorted(lst, key=str.lower)

    # 判断列表值是何类型1
    for i in range(len(lst)):
        _point_l.append([])
        _str_app_l.append([])
        for j in lst[i]:
            if 48 <= ord(j) <= 57:
                continue
            elif j == '.':
                if not _point_l[i]:
                    _point_l[i].append(True)
                else:
                    continue
            else:
                if not _str_app_l[i]:
                    _str_app_l[i].append(True)
                else:
                    continue

    # 判断列表值是何类型2
    for i in range(len(_point_l)):
        if True in _str_app_l[i]:
            _lst_types.append('str')
        elif True in _point_l[i] and _str_app_l[i] == []:
            for j in range(len(lst[i])):
                if lst[i][j] == '.':
                    _point_j += 1
            if _point_j == 1:
                _lst_types.append('float')
                _point_j = 0
            else:
                _lst_types.append('str')
                _point_j = 0
        else:
            _lst_types.append('int')

    # 转换类型
    for i in range(len(_lst_types)):
        if _lst_types[i] == 'str':
            if eval_mode:
                try:
                    lst[i] = eval(lst[i])
                except:
                    pass
            pass
        if _lst_types[i] == 'float':
            lst[i] = float(lst[i])
        if _lst_types[i] == 'int':
            lst[i] = int(lst[i])

    # code burger(bushi     (将收集到的特殊数据插入回列表)
    for i in range(len(_spe_type_content['complex'])):
        lst.remove(str(_spe_type_content['complex'][i]))
        lst.append(_spe_type_content['complex'][i])
    for i in range(len(_spe_type_content['tuple'])):
        lst.remove(str(_spe_type_content['tuple'][i]))
        lst.append(_spe_type_content['tuple'][i])
    for i in range(len(_spe_type_content['lst'])):
        lst.remove(str(_spe_type_content['lst'][i]))
        lst.append(_spe_type_content['lst'][i])
    for i in range(len(_spe_type_content['set'])):
        lst.remove(str(_spe_type_content['set'][i]))
        lst.append(_spe_type_content['set'][i])
    for i in range(len(_spe_type_content['dic'])):
        lst.remove(str(_spe_type_content['dic'][i]))
        lst.append(_spe_type_content['dic'][i])

    if bool_mode:
        for i in range(len(lst)):
            if lst[i] == 'True':
                lst[i] = bool(1)
            elif lst[i] == 'False':
                lst[i] = bool(0)

    return lst


def deeply_tidy_up_list(lst: list, bool_mode: bool = False, eval_mode: bool = False) -> list:
    """
    This Function can search list elements and tidy up it too(‾◡◝)

    :param bool_mode: If you want to turn such as 'True' into True which it is in this list and the elements in this list, you can turn on 'bool_mode' (～￣▽￣)～
    :param eval_mode: If you want to turn such as '[]' into [] which it is in this list and the elements in this list, you can turn on 'eval_mode' (￣◡￣)
    :param lst:put list which you need to sorting and clean（￣︶￣）
    :return: the perfect list  ( ´◡` )
    """

    if type(lst) is not list:
        return lst

    _j: int = 0
    lst = tidy_up_list(lst, bool_mode=bool_mode, eval_mode=eval_mode)

    for _i in lst:
        if type(_i) is list:
            lst[_j] = deeply_tidy_up_list(_i)
        _j += 1
    return lst


def bubble_sort(lst: list) -> list:
    """
    A simple bubble sort function ~(￣▽￣)~*\n
    (elements in the list can only be int)

    :param lst:
    :return:
    """

    try:
        lst_len = len(lst)
        for _i in range(lst_len):
            for _j in range(lst_len - 1 - _i):
                if lst[_j + 1] <= lst[_j]:
                    lst[_j], lst[_j + 1] = lst[_j + 1], lst[_j]
    except:
        raise ValueError('elements in the list cannot be of any type other than int')

    return lst
