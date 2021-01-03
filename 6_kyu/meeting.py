# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest
# come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same
# first name too.

# Notes

# You can see another examples in the "Sample tests".


def meeting(s):
    s = s.upper()
    first_and_last_name_strings = s.split(";")
    first_and_last_name_lists = [first_and_last_name_string.split(":") for first_and_last_name_string in first_and_last_name_strings]
    first_and_last_name_lists.sort(key=lambda first_and_last_name_list: [first_and_last_name_list[1], first_and_last_name_list[0]])
    last_and_first_name_strings = [f"({first_and_last_name_list[1]}, {first_and_last_name_list[0]})" for first_and_last_name_list in first_and_last_name_lists]

    return "".join(last_and_first_name_strings)
