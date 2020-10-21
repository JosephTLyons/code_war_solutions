# For this Kata you will have to forget how to add two numbers together.

# The best explanation on what to do for this kata is this meme :

# caf

# In simple terms our method does not like the principle of carrying over numbers and just writes
# down every number it calculates.

# You may assume both integers are positive integers and the result will not be bigger than
# Integer.MAX_VALUE (only for java)


def add(num1, num2):
    number_one_list = [int(digit) for digit in str(num1)]
    number_two_list = [int(digit) for digit in str(num2)]

    lists = [number_one_list, number_two_list]
    lists.sort(key=lambda x: len(x))

    while len(lists[0]) < len(lists[1]):
        lists[0].insert(0, 0)

    sum_list_strings = [str(lists[0][i] + lists[1][i]) for i in range(len(lists[0]))]

    return int("".join(sum_list_strings))
