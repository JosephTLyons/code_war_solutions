# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the
# "instructions" for the development and functioning of living organisms.

# If you want to know more http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have
# function with one side of the DNA (string, except for Haskell); you need to get the other
# complementary side. DNA strand is never empty or there is no DNA at all (again, except for
# Haskell).

# More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

# DNA_strand ("ATTGC") # return "TAACG"

# DNA_strand ("GTAT") # return "CATA"


def DNA_strand(dna):
    dna = swap_letters(dna, "A", "T", "Z")
    dna = swap_letters(dna, "G", "C", "Z")

    return dna

def swap_letters(text, letter_one, letter_two, temp_letter):
    text = text.replace(letter_one, temp_letter)
    text = text.replace(letter_two, letter_one)
    text = text.replace(temp_letter, letter_two)

    return text
