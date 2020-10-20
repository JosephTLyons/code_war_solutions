# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave
# punctuation marks untouched.

# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    word_list = text.split()
    punctuation_list = [".", "?", "!"]

    for i in range(len(word_list)):
        word = word_list[i]

        if word not in punctuation_list:
            continue

        pig_latin_word = word[1:] + word[0] + "ay"
        word_list[i] = pig_latin_word

    return " ".join(word_list)
