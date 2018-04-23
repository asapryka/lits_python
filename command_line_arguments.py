import argparse

parser = argparse.ArgumentParser(description='Process some formula and see if parenthesis are balanced.')
parser.add_argument('string', metavar='N', type=str, nargs='+',
                    help='enter a formula (string) to process')

args = parser.parse_args('(a-2)*(sqrt(4x)-6)**2')
list = list(args.__str__())
new_list = []

for n in list:
    if n in("(", ")"):
        new_list.append(n)

str = ''.join(new_list)
print(str)
l_side = str.count('(')
r_side = str.count(')')

if l_side == r_side:
    print("True")
else:
    print('False')

