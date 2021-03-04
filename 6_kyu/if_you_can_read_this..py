# The idea for this kata came from 9gag today:

# The lyrics to "Never gonna give you up" by Rick Astley encoded in the NATO phonetic alphabet

# Task

# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

# Input:

# If, you can read?

# Output:

# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

# Note:

# The set of used punctuation is .!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace


def to_nato(words):
    pilots_alphabet = {
        "a": "Alfa",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliett",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu",
    }

    pilots_sentence_list = []
    punctuation_list = [".", "?", "!"]

    for word in words:
        first_letter = word[0].lower()

        if first_letter in pilots_alphabet:
            pilots_word = pilots_alphabet[first_letter]
            pilots_sentence_list.append(pilots_word)
        elif first_letter in punctuation_list:
            pilots_sentence_list.append(first_letter)

    pilots_sentence = " ".join(pilots_sentence_list)

    return pilots_sentence
