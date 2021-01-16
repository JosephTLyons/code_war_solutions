# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]


def parse(data):
    output = 0
    output_list = []

    for operator in data:
        if operator == "i":
            output += 1
        elif operator == "d":
            output -= 1
        elif operator == "s":
            output **= 2
        elif operator == "o":
            output_list.append(output)

    return output_list
