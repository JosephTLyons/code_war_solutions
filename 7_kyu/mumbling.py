# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(s):
    string_list = []
    count = 1

    for letter in s:
        string_list.append(letter.lower() * count)
        count += 1

    string_list = [string.title() for string in string_list]

    final_string = "-".join(string_list)

    return(final_string)
