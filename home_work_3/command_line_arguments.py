import argparse
import sys

parser = argparse.ArgumentParser(description='Process some formula and see if parenthesis are balanced.')
parser.add_argument('string', metavar='N', type=str, nargs='+',
                    help='enter a formula (string) to process')

args = parser.parse_args(sys.argv[1:])
list = sys.argv[1:]
str = list[0]
str = str.strip("'")

new_list = []

for n in str:
    if n in("(", ")"):
        new_list.append(n)

print(new_list)
str_final = ''.join(new_list)

l_side = str_final.count('(')
r_side = str_final.count(')')

if l_side == r_side:
    print("True")
else:
    print('False')
