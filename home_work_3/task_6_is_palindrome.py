def is_palindrome(phrase):
    items_to_replace = {' ': ''}

    for i, j in items_to_replace.items():
        phrase = phrase.replace(i, j)

    phrase = phrase.lower()
    reverse = ''.join(reversed(phrase))

    if (phrase == reverse):
        return True
    return False

phrase = "0"
answer = is_palindrome(phrase)

if (answer):
    print("Yes")
else:
    print("No")

phrase = "puppy"
answer = is_palindrome(phrase)

if (answer):
    print("Yes")
else:
    print("No")

phrase = "mystring1Gni rts ym"
answer = is_palindrome(phrase)

if (answer):
    print("Yes")
else:
    print("No")