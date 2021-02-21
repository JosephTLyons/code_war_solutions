# You read the title.

# You must guess a sequence.

# It will have something to do with the number given.

# Example:

# x = 16

# result = [1, 10, 11, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9]


def sequence(x):
    number_strings = [str(i + 1) for i in range(x)]
    number_strings.sort()
    numbers = [int(i) for i in number_strings]

    return numbers
