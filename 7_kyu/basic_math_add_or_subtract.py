# In this kata, you will do addition and subtraction on a given string. The return value must be
# also a string.

# Note: the input will not be empty.

# Examples

# "1plus2plus3plus4"  --> "10"
# "1plus2plus3minus4" -->  "2"


import re


def calculate(s):
    operator_dict = {
        "plus": "+",
        "minus": "-",
    }

    for operator_name, operator_symbol in operator_dict.items():
        s = re.sub(operator_name, operator_symbol, s)

    return str(eval(s))
