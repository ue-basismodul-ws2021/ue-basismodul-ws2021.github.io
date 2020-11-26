def recursive_func(num, list_=None):
    if list_ is None:
        list_ = []
    if num == 0:
        return list_
    list_.append(num)
    return recursive_func(num - 1, list_)


print(recursive_func(5))
print(recursive_func(5))
