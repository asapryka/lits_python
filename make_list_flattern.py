
task = '''\nMake list flattern
lst = [1, [2, 3], 4, [[6, 7]]]
to
lst = [1, 2, 3, 4, 6, 7]'''
print(task)
print("Var1:")
lst = [1, [2, 3], 4, [[6, 7]]]
sin_lst = lst[1]
dbl_lst = list(lst[3])[0]

for n in sin_lst:
    lst.append(n)

for n in dbl_lst:
    lst.append(n)

lst.remove(lst[1])
lst.remove(lst[2])
lst.sort()
print('\n')
print(lst)

print("-----------------------------------------------------------")
print("Var2:\n\n")

lst = [1, [2, 3], 4, [[6, 7]]]
new_lst = []

for n in lst:
    if type(n) is list:
        lst_item_ind = lst.index(n)
        for x in lst[lst_item_ind]:
            lst.append(x)
    else:
        new_lst.append(n)
new_lst.sort()
print(new_lst)

print("-----------------------------------------------------------")



