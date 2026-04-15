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

#Example 4: try-except-else
try:
    num = int(input("Enter a numbers: "))
    result = num ** 2
except (ValueError) as e:
    print("Error: Value error: " , e)
   
else:
    print("The square of the number is: " , result)


# 5. What is the purpose of the finally block?
try:
    a = int(input("Enter a number: "))
    result = a ** 2
    print("The square of the number is: " , result)
except (ValueError) as e:
    print("Error: Value error: " , e)
   
else:
    print("The square of the number is: " , result)
finally:
    print("Thank you")



# try:
#     a = int(input())
#     b = int(input())
#     c = [1, 2, 3]
#     d = a / b
#     d = [5]
#     print(d)
# except (ZeroDivisionError) as e:
#     print('Error ' , e)
# except (ValueError) as e:
#     print('Error', e)
# except (IndexError) as e:
#     print('Error: ', e)
# except Exception as e:
#     print("Error: Exception: " , e)
# finally:
#     print("Thank you")



## Raise key word

age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You are not old enough to vote")
elif age > 65:
    raise ValueError("You are too old to vote")
else:
    print("You are eligible to vote")


def calculate_square_root(number):
    if number < 0: 
        raise ValueError("Cannot calulate the square root of a negative numbers")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
    print(f"The result is: {result}")
except ValueError as e:
    print(f"Error: {e}")
