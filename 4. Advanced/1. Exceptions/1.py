# 1. What is an exception?
# ans: An exception is an event that disrupts the normal flow of the program.

# 2. What is the purpose of the try-except block?

#Handle exceptions
#Example 1: Division by zero
try:
    a = 10 / 0
except (ZeroDivisionError) as e:
    print("Error: Division by zero: " , e)

print("Thank you")

#Example 2: File not found
try:
    f = open("file.txt", "r")
except (FileNotFoundError) as e:
    print("Error: File not found: " , e)
print("Thank you")

#Example 3: Keyboard interrupt

try:
    a = int(input("Enter a number: "))
except (KeyboardInterrupt) as e:
    print("Error: Keyboard interrupt: " , e)

print("Thank you")


# 4 Multiple except blocks
try:
    a = int(input("Enter a number: "))
except (KeyboardInterrupt) as e:
    print("Error: Keyboard interrupt: " , e)
except (ValueError) as e:
    print("Error: Value error: " , e)
except (TypeError) as e:
    print("Error: Type error: " , e)

#Generic except block
except Exception as e:
    print("Error: Exception: " , e)

print("Thank you")