# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]


def multiplication_table(size):
    result = []
    multiplier = 1

    for i in range(size):
        row = [(j + 1) * multiplier for j in range(size)]
        result.append(row)
        multiplier += 1

    return result
