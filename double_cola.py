# Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending
# machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can,
# drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the
# queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

# For example, Penny drinks the third can of cola and the queue will look like this:

# Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
# Write a program that will return the name of the person who will drink the n-th cola.

# Input:

# The input data consist of an array which contains at least 1 name, and single integer n which may
# go as high as the biggest number your language of choice supports (if there's such limit, of
# course).

# Output / Examples:

# Return the single line — the name of the person who drinks the n-th can of cola. The cans are
# numbered starting from 1.

# who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
# who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
# who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"


from collections import deque


def who_is_next(names, r):
    name_occurrence_deque = deque([name, 1] for name in names)

    while r > 0:
        if r <= name_occurrence_deque[0][1]:
            break
        else:
            r -= name_occurrence_deque[0][1]
            name_occurrence_deque[0][1] *= 2
            name_occurrence_deque.rotate(-1)

    return name_occurrence_deque[0][0]
