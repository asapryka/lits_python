
task = '''\nCheck if parenthesis are balanced
str = '((((((((((((((2, 3)))))))))))))'''
print(task)

str = '((((((((((((((2, 3)))))))))))))'

l_side = str.count('(')
r_side = str.count(')')

print('\n')

if l_side == r_side:
    print("Success! Parenthesis are balanced!")
else:
    print('Missed! Parenthesis are not balanced, please count again.')
    print('There are %i from the left,' % l_side)
    print('and %i from the right.' % r_side)
print("-----------------------------------------------------------")