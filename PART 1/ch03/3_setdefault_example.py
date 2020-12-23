# 3.2.1 딕셔너리 메소드


def usual_dict(dict_data):
    """ dict[key] 사용 """
    new_data = {}
    for k, v in dict_data:
        if k in new_data:
            new_data[k].append(v)
        else:
            new_data[k] = [v]           # key 값이 없으면 리스트로 추가함
    return new_data


def setdefault_dict(dict_data):
    """ setdefault() 메소드 사용 """
    new_data = {}
    for k, v in dict_data:
        new_data.setdefault(k, []).append(v)            # 딕셔너리에 존재하지 않은 키에 접근하면 에외 발생
    return new_data


def test_setdef():
    dict_data = (("key1", "value1"),
                 ("key1", "value2"),
                 ("key2", "value3"),
                 ("key2", "value4"),
                 ("key2", "value5"))
    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))


if __name__ == '__main__':
    test_setdef()
