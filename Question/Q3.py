# Student Fee Calculator
#
# A training institute offers a scholarship scheme where the discount decision is represented only as a boolean value.
#
# You are required to calculate the final payable course fee for a student based on the following details:
#
# Accept the student name as a string.
# Accept the base course fee as a float.
# Accept the scholarship status as a boolean value (True or False).
# Rules to calculate the final fee:
#
# A student with a scholarship is eligible for a 10% reduction on the base fee.
# After applying the discount (if any), an 18% GST must be added.
# The calculation logic must be written inside a function that:
# Takes the base fee and scholarship status as parameters
# Returns the final payable amount
# Print the student name along with the final fee.
from typing import final


def calculate_final_fee(base_fee: float, has_scholarship: bool) -> float:
    """
    Calculate final payable fee without using if/else.
    """
    # Scholarship discount factor: 0.9 if True else 1.0
    discount_factor = 1 - (0.10 * has_scholarship)

    # Apply discount
    discounted_fee = base_fee * discount_factor

    # Add 18% GST
    final_fee = discounted_fee * 1.18

    return final_fee


# Input section
student_name = input("Enter student name: ")
base_fee = float(input("Enter base course fee: "))
scholarship_status = input("Scholarship status (True/False): ").strip().lower() == "true"

# Calculate final fee
final_amount = calculate_final_fee(base_fee, scholarship_status)

# Print result
print(f"Student: {student_name}, Final Payable Fee: ₹{final_amount:.2f}")