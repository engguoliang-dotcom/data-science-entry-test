def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap using arithmetic without a third variable
    x = x + y  # x now holds the sum of both numbers
    y = x - y  # y becomes the original value of x
    x = x - y  # x becomes the original value of y
    
    print(f"Swapped values: x = {x}, y = {y}")


# Task 2
# Invoke the function "swap" using the provided scenarios:

print("Scenario 1: 'Apple', 10")
result_1 = swap("Apple", 10)
if result_1 == -1:
    print("Return value:", result_1)

print("\nScenario 2: 9, 17")
swap(9, 17)
