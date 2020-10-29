# Task

# In this kata you will be given a list consisting of unique elements except for one thing that
# appears twice.

# Your task is to output a list of everything inbetween both occurrences of this element in the
# list.

# Examples:

# [0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
# ['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
# [0, 0] => []
# [True, False, True] => [False]
# ['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']
# Notes

# All elements will be the same datatype.
# All used elements will be hashable.


def duplicate_sandwich(arr):
    name_occurrence_dictionary = {}

    slice_start = 0
    slice_end = 0

    for index, item in enumerate(arr):
        if item in name_occurrence_dictionary:
            slice_start = name_occurrence_dictionary[item]
            slice_end = index
            break
        else:
            name_occurrence_dictionary[item] = index

    return arr[slice_start + 1:slice_end]
