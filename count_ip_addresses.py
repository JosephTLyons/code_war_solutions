# Implement a function that receives two IPv4 addresses, and returns the number of addresses between
# them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be
# greater than the first one.

# Examples

# ips_between("10.0.0.0", "10.0.0.50")  ==   50
# ips_between("10.0.0.0", "10.0.1.0")   ==  256
# ips_between("20.0.0.10", "20.0.1.0")  ==  246


def get_number_list(ip_address_string):
    numbers = ip_address_string.split(".")
    return [int(number) for number in numbers]

def ips_between(start, end):
    start_numbers = get_number_list(start)
    end_numbers = get_number_list(end)

    difference = [end_numbers[i] - start_numbers[i] for i in range(len(start_numbers))]

    sum = 0

    diff_len = len(difference) - 1

    for index, num in enumerate(difference):
        reverse_index = diff_len - index
        sum += num * 256 ** reverse_index

    return sum
