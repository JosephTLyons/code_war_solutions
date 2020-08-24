# Description:

# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

# Your task is to process a string with "#" symbols.

def clean_string(s):
    letters = []

    for i in range(len(s)):
        character = s[i]

        if character == "#":
            letters.pop()
        else:
            letters.append(character)

    return "".join(letters)
