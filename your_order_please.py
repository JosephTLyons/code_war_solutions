# Your task is to sort a given string. Each word in the string will contain a single number. This
# number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only
# contain valid consecutive numbers.

# Examples
#     "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#      "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#      ""  -->  ""


def order(sentence):
    words = sentence.split()
    number_to_word_dict = {}

    for word in words:
        for character in word:
            try:
                num = int(character)
                number_to_word_dict[num] = word
            except:
                pass

    final_sentence = ""

    dict_length = len(number_to_word_dict)

    for i in range(dict_length):
        final_sentence += number_to_word_dict[i + 1]

        if i < dict_length - 1:
            final_sentence += " "

    return final_sentence
