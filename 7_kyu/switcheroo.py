# Given a string made up of letters a, b, and/or c, switch the position of letters a and b
# (change a to b and vice versa). Leave any incidence of c untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'


def switcheroo(string):
    string = string.replace("a", "z")
    string = string.replace("b", "a")
    string = string.replace("z", "b")

    return string
