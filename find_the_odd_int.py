# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    number_to_occurrence_dictionary = {}

    for number in seq:
        if number in number_to_occurrence_dictionary:
            number_to_occurrence_dictionary[number] += 1
        else:
            number_to_occurrence_dictionary[number] = 1

    print(number_to_occurrence_dictionary)

    for number, occurrence in number_to_occurrence_dictionary.items():
        if occurrence % 2 == 1:
            return number

    return None
