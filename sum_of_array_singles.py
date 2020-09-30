# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest
# occur only twice. Your task will be to return the sum of the numbers that occur only once.

# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their
# sum is 15.

# More examples in the test cases.

# Good luck!


def repeats(arr):
    number_freq_dict = {}

    for number in arr:
        if number in number_freq_dict:
            number_freq_dict[number] = False
        else:
            number_freq_dict[number] = True

    sum = 0

    print(number_freq_dict)

    for number, freq in number_freq_dict.items():
        if freq:
            sum += number

    return sum
