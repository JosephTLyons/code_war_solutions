# Given a string of binary numbers of length 3 sort the numbers in ascending order but only order
# the even numbers and leave all odd numbers in their place.

# Example:

# even_binary("101 111 100 001 010") # returns "101 111 010 001 100"
# Note: make sure all the binary numbers have a length of 3


def even_binary(n):
    marker_symbol = "*"
    binary_strings = n.split()
    even_binary_strings = []
    remaining_binary_strings = []

    for number_string in binary_strings:
        if number_string.endswith("0"):
            even_binary_strings.append(number_string)
            remaining_binary_strings.append(marker_symbol)
        else:
            remaining_binary_strings.append(number_string)

    print(remaining_binary_strings)

    even_binary_strings.sort(key=lambda even_binary_string: int(even_binary_string, 2))
    final_binary_string = " ".join(remaining_binary_strings)

    for even_binary_string in even_binary_strings:
        final_binary_string = final_binary_string.replace(marker_symbol, even_binary_string, 1)

    return final_binary_string
