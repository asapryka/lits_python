import sys

def lab(argv):
    """ Return True if the parentheses in command-line argument match, otherwise False. """
    j = 0
    for c in sys.argv[1:]:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0

for i, sys.argv[1:] in enumerate(sys.argv[1:]):
    print(sys.argv[1:])
    print(lab(sys.argv[1:]))
