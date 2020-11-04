# Given a string, return true if the first instance of "x" in the string is immediately followed by
# the string "xx".

# tripleX("abraxxxas") → true
# tripleX("xoxotrololololololoxxx") → false
# tripleX("softX kitty, warm kitty, xxxxx") → true
# tripleX("softx kitty, warm kitty, xxxxx") → false
# Note :

# capital X's do not count as an occurrence of "x".
# if there are no "x"'s then return false


def triple_x(s):
    x_index = s.find("x")
    print(x_index)

    if x_index == -1 or len(s) - x_index < 3:
        return False

    if s[x_index + 1] == "x" and s[x_index + 2] == "x":
        return True

    return False
