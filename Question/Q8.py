# Write a Python function called alternating_harmonic_sum that takes a positive integer n as input.
# Using only a while loop, variables, basic data types (like integers and floats), and arithmetic operators,
# compute the sum of the alternating harmonic series up to n terms: 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^{n+1}/n.
# The function should handle the sign alternation cleverly without using any conditional statements inside
# the loop (hint: think about clever use of operators or variables to flip the sign each iteration).
# Return the sum as a float rounded to 4 decimal places. Make sure it works for
#  n=1 (sum=1.0000) and larger values like n=10000 without inefficiency.

# Function name: alternating_harmonic_sum(n)
#
# Steps should follow:
#
# Define function that takes one parameter n
# Create variable total and set it to 0.0
# Create variable sign and set it to 1.0
# Create variable i and set it to 1
# Start a while loop that runs while i <= n
# Inside the loop:
# Calculate term = sign * (1.0 / i)
# Add term to total → total = total + term
# Change sign for next term → sign = sign * -1.0
# Increase counter → i = i + 1
# After loop ends, create variable result = round(total, 4)
# Return result

def alternating_harmonic_sum(n):
    total = 0.0
    sign = 1.0
    i = 1
    while i <= n:
        term = sign * (1.0 / i)
        total += term
        sign *= -1.0
        i += 1
        result = round(total , 4)
        return result
print(alternating_harmonic_sum(9000000))

