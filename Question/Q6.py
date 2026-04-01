# Alternating Square Series Calculator
#
# Write a Python program to build a function-based solution that calculates a special mathematical series.
#
# The program should perform the following steps:
#
# Define a function named alternating_square_sum() that accepts one integer parameter n.
# Inside the function, use only a for loop and arithmetic operators to compute the series:
# 12−22+32−42+52−...±n2
#
# The function must return the final computed result.
# In the main part of the program:
# Take the value of n from the user.
# Call the function by passing n as an argument.
# Store the returned value in a variable.
# Display the final output in a readable format.
# Note: Do not use any advanced Python features other than functions and for loop.

def alternating_squares_sum(n):
    total_sum = 0
    sing = 1
    for i in range(1, n + 1):
        total_sum = total_sum + sing * (i * i)
        sing = sing * -1
    return total_sum


print(int(alternating_squares_sum(5)))
