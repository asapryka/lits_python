import string

def convert_n_to_m(x, n, m):
    alphabet = string.digits + string.ascii_uppercase
    result = []

    while n < 1 or m > 36:
        print("You entered incorrect value, please enter 1 >= n and m <= 36")
        break

    if isinstance(x, str):
        number = 0
        for i in range(len(x)):
            number += alphabet.index(x[i]) * (n ** (len(x) - i - 1))
    else:
        number = int(x)

    # convert to number system "m"
    while number > m:
        cile_chyslo = number // m
        ostacha = number - (cile_chyslo * m)
        result.append(alphabet[ostacha])
        number = cile_chyslo

    result.append(alphabet[number])
    converted_to_m_list = list(reversed(result))
    converted_to_m_string = ''.join(converted_to_m_list)
    print(converted_to_m_string)
    return converted_to_m_string


convert_n_to_m("001101010001110", 2, 8)
