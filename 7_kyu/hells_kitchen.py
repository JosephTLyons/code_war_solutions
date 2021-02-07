# Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.

# Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.

# Rules:

# Obviously the words should be Caps, Every word should end with '!!!!', Any letter 'a' or 'A'
# should become '@', Any other vowel should become '*'.


def gordon(a):
    word_string = a.upper()
    letter_to_replacement_symbol_dictionary = {
        "A": "@",
        "E": "*",
        "I": "*",
        "O": "*",
        "U": "*",
    }

    for letter, replacement_symbol in letter_to_replacement_symbol_dictionary.items():
        word_string = word_string.replace(letter, replacement_symbol)

    words = word_string.split()
    words = [word + "!!!!" for word in words]

    return " ".join(words)
