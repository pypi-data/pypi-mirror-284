from typing import Union


def tidy_up_list(lst: Union[list, dict, set, tuple], bool_mode: bool = False, eval_mode: bool = False) -> list:
    """

    :param bool_mode: If you want to turn such as 'True' into True which it is in this list, you can turn on 'bool_mode' (～￣▽￣)～
    :param eval_mode: If you want to turn such as '[]' into [] which it is in this list, you can turn on 'eval_mode' (￣◡￣)
    :param lst:put list which you need to sorting and clean （￣︶￣）
    :return: the perfect list  ( ´◡` )

    """

    _lst_types: list = []
    _point_j: int = 0
    _point_l: list = []
    _str_app_l: list = []
    _spe_type_content: dict = {'lst': [], 'dic': [], 'set': [], 'tuple': [], 'complex': []}

    for i in range(len(lst)):
        if type(lst[i]) is list:
            _spe_type_content['lst'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is dict:
            _spe_type_content['dic'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is set:
            _spe_type_content['set'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is tuple:
            _spe_type_content['tuple'].append(lst[i])
            lst[i] = str(lst[i])
        elif type(lst[i]) is complex:
            _spe_type_content['complex'].append(lst[i])
            lst[i] = str(lst[i])

    lst = set(lst)
    lst = list(lst)
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    lst = sorted(lst, key=str.lower)

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

    for i in range(len(_lst_types)):
        if _lst_types[i] == 'str':
            if eval_mode:
                try:
                    lst[i] = eval(lst[i])
                except:
                    pass
        if _lst_types[i] == 'float':
            lst[i] = float(lst[i])
        if _lst_types[i] == 'int':
            lst[i] = int(lst[i])

    for i in range(len(_spe_type_content['complex'])):
        lst.remove(str(_spe_type_content['complex'][i]))
        lst.append(_spe_type_content['complex'][i])
    for i in range(len(_spe_type_content['tuple'])):
        lst.remove(str(_spe_type_content['tuple'][i]))
        lst.append(_spe_type_content['tuple'][i])
    for i in range(len(_spe_type_content['lst'])):
        lst.remove(str(_spe_type_content['lst'][i]))
        lst.append(_spe_type_content['lst'][i])
    for i in range(len(_spe_type_content['dic'])):
        lst.remove(str(_spe_type_content['dic'][i]))
        lst.append(_spe_type_content['dic'][i])
    for i in range(len(_spe_type_content['set'])):
        lst.remove(str(_spe_type_content['set'][i]))
        lst.append(_spe_type_content['set'][i])

    if bool_mode:
        for i in range(len(lst)):
            if lst[i] == 'True':
                lst[i] = bool(1)
            elif lst[i] == 'False':
                lst[i] = bool(0)

    return lst
