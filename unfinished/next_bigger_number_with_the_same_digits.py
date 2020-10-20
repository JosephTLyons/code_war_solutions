# Create a function that takes a positive integer and returns the next bigger number that can be
# formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil

import itertools


def next_bigger(n):
    digit_list = [int(digit) for digit in str(n)]

    digit_permutation_tuples = list(itertools.permutations(digit_list))

    final = []

    for permutation_tuple in digit_permutation_tuples:
        number_string = ""

        for digit in permutation_tuple:
            number_string += str(digit)

        final.append(int(number_string))

    final = list(set(final))
    final.sort()

    index_of_original_number = final.index(n)

    return final[index_of_original_number + 1]
