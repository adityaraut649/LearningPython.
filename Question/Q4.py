# Banking Balance Evaluator

# A bank records all transaction outcomes using numeric values, where the nature of the final balance is determined only through expressions, not decisions.

# You are required to compute and evaluate a customer’s final bank balance using the following details:

# Inputs:

# Accept the initial balance as an integer.
# Accept the deposit amount as an integer.
# Accept the withdrawal amount as an integer.
# Processing Rules:

# The final balance is calculated by adding the deposit amount to the initial balance and then subtracting the withdrawal amount.
# The balance evaluation must be done without using any decision-making statements.
# The program should determine whether the final balance is non-negative or negative using comparison operators and store the result.
# Functional Requirement:

# Write a function that:
# Takes the initial balance, deposit amount, and withdrawal amount as parameters
# Returns the final balance
# After calling the function:
# Display the final balance
# Display the result of the balance evaluation (True or False)
# Convert initial_balance to int immediately


initial_bal = int(input("Enter initial balance: "))
deposit = int(input("Enter deposit: "))
withdrawal = int(input("Enter withdrawal: "))

def bank(initial_bal: int, deposit: int, withdrawal: int):
    final_balance = initial_bal + deposit - withdrawal
    return final_balance > 0
print(bank(initial_bal, deposit, withdrawal))


