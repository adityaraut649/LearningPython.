# Write a Python program that demonstrates how the bitwise complement operator relates to integer negation. Your program should:
#
#     • Take one input from the user and store it in a variable n.
#
#     • Convert the input to an integer.
#
#     • Apply the bitwise complement (~) operator on the integer.
#
#     • Add 1 to the result.
#
#     • Compare the final value with the negative of the original number.
#
#     • Print the boolean result.




n = input()
n = int(n)
n = ~n
n = n + 1
print(n == ~(-5))
