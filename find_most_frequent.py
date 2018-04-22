import collections

def find_most_frequent(text):
    items_to_replace = {',': ' ', '.': ' ', ':': ' ', ';': ' ', '!': ' ', '?': ' ', '-': ' '}
    result_list = []

    for i, j in items_to_replace.items():
        text = text.replace(i, j)

    for item, count in collections.Counter(text.split()).items():
        if count > 1:
            result_list.append(item)

    result_list = [element.lower() for element in result_list];

    print(result_list)
    return result_list

# find_most_frequent("Hello,Hello, my dear!")

# find_most_frequent("to understand recursion you need first to understand recursion...")

find_most_frequent("Mom! Mom!Are you sleeping?!!!")