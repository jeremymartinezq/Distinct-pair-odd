# lastname_firstname_weekNumber.py
# Author: JEREMY MARTINEZ
# PID: 3487500
# Submission Date: SEP 19, 2024

# Program Summary:
# This script defines a function that checks whether there exists a distinct pair
# of numbers in a list whose product is odd. It will return True if such a pair exists
# and False otherwise. An odd product is only possible if both numbers are odd.

def has_odd_pair(data):
    """This function takes a list of integers and checks if there is a distinct pair
    of odd numbers whose product is odd. Returns True if such a pair exists,
    False otherwise"""
    odd_count = 0  # Count of odd numbers found

    # Iterate over the data
    for number in data:
        if number % 2 != 0:  # If the number is odd
            odd_count += 1
            if odd_count == 2:  # If we find 2 odd numbers, return True
                return True

    # If less than 2 odd numbers, return False
    return False

# Driver Code:
if __name__ == "__main__":
    # Example 1: There is a pair of odd numbers (7 and 9), so it returns True
    example_data_1 = [4, 8, 7, 9]
    print(f"Does {example_data_1} have an odd product pair? {has_odd_pair(example_data_1)}")
    # Expected output: True

    # Example 2: There is only one odd number (5), so it returns False
    example_data_2 = [2, 4, 5, 6]
    print(f"Does {example_data_2} have an odd product pair? {has_odd_pair(example_data_2)}")
    # Expected output: False

    # Example 3: There are no odd numbers, so it returns False
    example_data_3 = [2, 4, 6, 8]
    print(f"Does {example_data_3} have an odd product pair? {has_odd_pair(example_data_3)}")
    # Expected output: False
