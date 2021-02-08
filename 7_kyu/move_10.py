# Move every letter in the provided string forward 10 letters through the alphabet.

# If it goes past 'z', start again at 'a'.

# Input will be a string with length > 0.


def move_ten(st):
    transformed_text = ""

    for letter in st:
        letter_value = ord(letter) - ord("a")
        letter_value += 10
        letter_value %= 26
        letter_value += ord("a")

        transformed_text += chr(letter_value)

    return transformed_text
