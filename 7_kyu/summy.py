# Write a function that takes a string which has integers inside it separated by spaces, and your 
# task is to convert each integer in the string into an integer and return their sum.
# Example

# summy("1 2 3")  ==> 6


def summy(string_of_ints):
    strint_int_list = string_of_ints.split()
    int_list = [int(string_int) for string_int in strint_int_list]

    return sum(int_list)
