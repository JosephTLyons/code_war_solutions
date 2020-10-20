# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.


def find_short(s):
    words_list = s.split()
    words_length_list = [len(word) for word in words_list]

    return min(words_length_list)
