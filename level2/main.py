import math
import numpy

def count_letter(string: str, letter):
    counter = 0

    for i in string:
        if i == letter:
            counter += 1

    return counter

def update_dict(dictionary: list, string):
    first_letter = string[0]
    breaker = 0

    for i in range(0, len(dictionary)):
        if dictionary[i][0] == first_letter:
            breaker = 1

    if breaker == 0:
        _tuple = (first_letter, 0)
        dictionary.append(_tuple)

    print(dictionary)
    return dictionary

# tuple (letter, amount)
def validate_string(string: str, dictionary: list):
    for letter in string:
        for i in range(0, len(dictionary)):
            if dictionary[i][0] == letter:
                dictionary[i] = (letter, dictionary[i][1]+1)
                print(letter, dictionary[i][1])

def print_results(dictionary: list):
    for i in range(0, len(dictionary)):
        print(dictionary[i][1])

file = open("level1 (1)/level1_1.in")
amount = int(file.readline())

diction = []

for i in range(0, amount):
    line = file.readline()
    # print(line)
    diction = update_dict(diction, line)

file.close()

file = open("level1 (1)/level1_1.in")
amount = int(file.readline())

for i in range(0, amount):
    line = file.readline()
    validate_string(line, diction)

file.close()

# print(diction)
print_results(diction)

# print(count_letter(text, 'B'))

# file.close()