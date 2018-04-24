def counter(a, b):
    a = list(str(a))
    b = list(str(b))
    print(len(set(a) & set(b)))

counter(12345, 567)
counter(1233211, 12128)
counter(123, 45)