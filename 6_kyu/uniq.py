# Implement a function which behaves like the uniq command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

# Example:
# ["a", "a", "b", "b", "c", "a", "b", "c"]  =>  ["a", "b", "c", "a", "b", "c"]


def uniq(seq):
    characters = []

    for item in seq:
        if len(characters) == 0 or characters[-1] != item:
            characters.append(item)

    return characters
