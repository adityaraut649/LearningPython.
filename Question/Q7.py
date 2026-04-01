# Write a Python program that analyzes a number and returns different data types based on conditions.
#
# The program should follow these steps:
#
# Define a function named smart_operation() that takes one integer argument n.
# Inside the function:
# If the number is divisible by both 3 and 5, return the string "Python".
# If the number is divisible only by 3, return twice the number as an integer.
# If the number is divisible only by 5, return half of the number as a float.
# Otherwise, return the boolean value False.
# In the main program:
# Accept input from the user.
# Call the function.
# Print the returned value and also print the data type of the returned value.
# Note: The solution must strictly use variables, data types, operators, functions, and only for loop if needed.


def smart_operation(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Python"
    elif n % 3 == 0:
        return n * 2
    elif n % 5 == 0:
        return float(n / 2)
    else:
        return False


n = int(input("Enter a number: "))
result = smart_operation(n)
print("Result: ",result)
print("Data type: ",type(result))


