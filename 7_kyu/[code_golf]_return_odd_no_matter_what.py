# Given the integer n return odd numbers as they are, but subtract 1 from even numbers.

# Note:

# if python:

# Your solution should be 36 or less characters long.

# if javascript:

# The length of function's body (without name of function) should be 12 or less characters long.

# Examples

# Input  = 2
# Output = 1

# Input  = 13
# Output = 13

# Input  = 46
# Output = 45

# NOTE: I'm not a fan of this formatting, but the final solution could be no more than 36
# characters, which was the exact length of my solution.


def always_odd(n):return n-((n-1)%2)
