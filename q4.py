def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if the input is a string to satisfy the requirement
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
        
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
result_1 = string_reverse("Hello World")
result_2 = string_reverse("Python")

# Printing the results to verify
print(result_1)  # Output: dlroW olleH
print(result_2)  # Output: nohtyP
