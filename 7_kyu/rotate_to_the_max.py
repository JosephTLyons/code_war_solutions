# Task

# Given a number, return the maximum value by rearranging its digits.

# Examples:

# (123) => 321 (786) => 876 ("001") => 100 (999) => 999 (10543) => 54310

# ^Note the number may be given as a string


def rotate_to_max(n):
    digit_string_list = [digit_string for digit_string in str(n)]
    digit_string_list.sort(reverse=True)

    largest_number = int("".join(digit_string_list))

    return largest_number
