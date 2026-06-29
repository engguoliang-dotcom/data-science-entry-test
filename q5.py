def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Ensure both inputs are numeric (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric.")
    
    # Avoid division by zero
    if divisor == 0:
        return False
        
    # Check if the remainder is 0
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the provided scenarios:
result_1 = check_divisibility(10, 2)
result_2 = check_divisibility(7, 3)

print(f"Is 10 divisible by 2? {result_1}")  # Expected: True
print(f"Is 7 divisible by 3? {result_2}")   # Expected: False
