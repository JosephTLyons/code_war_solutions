# You will be given an array of numbers.

# For each number in the array you will need to create an object.

# The object key will be the number, as a string. The value will be the corresponding character
# code, as a string.

# Return an array of the resulting objects.

# All inputs will be arrays of numbers. All character codes are valid lower case letters. The input
# array will not be empty.


def num_obj(s):
    objects_list = []

    for number in s:
        number_string = str(number)
        character = chr(number)
        objects_list.append({number_string: character})

    return objects_list
