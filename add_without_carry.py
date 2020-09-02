# For this Kata you will have to forget how to add two numbers together.

# The best explanation on what to do for this kata is this meme :

# caf

# In simple terms our method does not like the principle of carrying over numbers and just writes
# down every number it calculates.

# You may assume both integers are positive integers and the result will not be bigger than
# Integer.MAX_VALUE (only for java)

# Note: The actual name of this Kata is 16 + 18 = 214


def add(num1, num2):
    number_one_list = [int(digit) for digit in str(num1)]
    number_two_list = [int(digit) for digit in str(num2)]

    if len(number_one_list) > len(number_two_list):
        larger_list = number_one_list
        smaller_list = number_two_list
    else:
        larger_list = number_two_list
        smaller_list = number_one_list

    while len(smaller_list) < len(larger_list):
        smaller_list.insert(0, 0)

    sum_list_strings = [str(larger_list[i] + smaller_list[i]) for i in range(len(larger_list))]

    return int("".join(sum_list_strings))
