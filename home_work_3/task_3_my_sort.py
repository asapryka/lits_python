def my_sort(func, array, reverse):
    """this function sorts an array"""
    # type: (func, list, bool) -> list
    if type(array) != list:
        print('"array" parameter is not a list.')
    else:
        array.sort()
        if func:
            array.sort(key=func)
        if reverse:
            array.reverse()

        print(array)


my_sort(None, ["Aa", "cCc", "bbbbb", "a"], None)

my_sort(None, ["Aa", "cCc", "bbbbb", "a"], reverse=True)

my_sort(lambda x: len(x), ["Aa", "cCc", "bbbbb", "a"], None)

