# The Secret Password Validator Game
#
# 1. Write a function called check_secret_code() that does all of the following:
#
# 1. The function takes one parameter: attempts_allowed (an integer ≥ 1)
# 2. Inside the function you must:
# Ask the user to enter a secret code (using input())
# The real secret code is the 6-digit number: 251983
# 3. Rules for a valid attempt:
# The entered code must be exactly 6 characters long
# All characters must be digits (0–9)
# The sum of the digits must be exactly 28
# The product of the six digits must be greater than 400
# The third digit must be odd
# The number formed by the last two digits must be divisible by 7
# 4. Behavior:
# If the entered code satisfies all six rules above → print "Access granted! You are the chosen one." and immediately exit the function (return)
# If the code is wrong → print one of these messages (choose the most serious reason only – in this priority order):
# "Length must be exactly 6 digits!"
# "Only digits 0-9 are allowed!"
# "Digit sum must be exactly 28"
# "Product of digits must be > 400"
# "Third digit must be odd"
# "Last two digits must form number divisible by 7"
# The user gets exactlyattempts_allowed tries
# Use a while loop + counter + break when access is granted
# After each failed attempt, print how many attempts are remaining (example: "Attempts remaining: 2")
# After all attempts are used up without success → print "All attempts failed. Security system locked!"
# Outside the function: call check_secret_code



# def check_secret_code(attempts_allowed):
#     sum_of = 28
#     product_of_all = 500
#     print(f"You have {attempts_allowed} attempts to enter the secret code of 6 digits")
#
#     attempts = 0
#     while attempts < attempts_allowed:
#         remaining  = attempts_allowed - attempts
#         print(f"You have {remaining} attempts to enter the secret code of 6 digits")
#
#         code = input("Enter your secret code: ").strip()
#
#         attempts += 1
#
#         if len(code) != 6
#             print("length of the code must be 6")
#             continue
#
#         #check for digits
#
#
#         if check_secret_code(code):
#             sum_of += int(code)
#             continue


