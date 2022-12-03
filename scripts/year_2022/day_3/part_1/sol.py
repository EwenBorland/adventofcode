import string
# split string and create two halves , find duplicates in two lists


def get_lists(line):
    half = len(line)//2
    return line[:half], line[half:]

def get_duplicate_items_all(input):
    items = []
    for line in input:
        list_1, list_2 = get_lists(line)
        items += get_duplicate_items(list_1, list_2)
    return items

def get_duplicate_items(list_1, list_2):
    return list(set(list_1).intersection(list_2))

def sum_priorities(items):
    values = []
    for letter in items:
        if letter.isupper():
            values.append(ord(letter)- 38)
        else:
            values.append(ord(letter)- 96)
    return sum(values)

def solution(input):
    items = get_duplicate_items_all(input)
    return sum_priorities(items)
