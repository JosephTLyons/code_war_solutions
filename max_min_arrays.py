# In this Kata, you will be given an array of unique elements, and your task is to rerrange the
# values so that the first max value is followed by the first minimum, followed by second max value
# then second min value, etc.

# For example:

# solve([15,11,10,7,12]) = [15,7,12,10,11]
# The first max is 15 and the first min is 7. The second max is 12 and the second min is 10 and so
# on.

# More examples in the test cases.

# Good luck!



def solve(arr):
    arr.sort()
    max_min_arr = []
    count = 0

    while arr:
        if count % 2 == 0:
            index = -1
        else:
            index = 0

        max_min_arr.append(arr[index])
        del arr[index]

        count += 1

    return max_min_arr
