# Description:

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of
# those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!


def create_phone_number(n):
    first = make_number_string(n[0:3])
    second = make_number_string(n[3:6])
    third = make_number_string(n[6:10])

    return "({}) {}-{}".format(first, second, third)


def make_number_string(n):
    return "".join(str(num) for num in n)
