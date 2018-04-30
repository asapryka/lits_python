def count_holes(n):

    number_of_holes = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 0,
        "6": 1,
        "7": 0,
        "8": 2,
        "9": 1,
        "0": 1
    }

    numbers_with_holes = []

    if type(n) is int:
        string_number = str(n)
        string_number = string_number.lstrip("0")
        for i in string_number:
            if i in number_of_holes:
                numbers_with_holes.append(number_of_holes.get(str(i)))
        print(sum(numbers_with_holes))

    elif type(n) is str:
        n = n.lstrip("0")
        for i in n:
            if str(i) in number_of_holes:
                numbers_with_holes.append(number_of_holes.get(str(i)))
        print(sum(numbers_with_holes))

    else:
        print("ERROR")


count_holes("123")
count_holes(906)
count_holes("001")
count_holes(-8)
count_holes(-8.0)
