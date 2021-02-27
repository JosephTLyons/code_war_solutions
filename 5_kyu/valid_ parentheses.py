# Write a function that takes a string of parentheses, and determines if the order of the
# parentheses is valid. The function should return true if the string is valid, and false if it's
# invalid.

# Examples

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints

# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat
# other forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string):
    unmatched_opens = 0

    for character in string:
        if character == "(":
            unmatched_opens += 1
        elif character == ")":
            if unmatched_opens > 0:
                unmatched_opens -= 1
            else:
                return False

    return unmatched_opens == 0
