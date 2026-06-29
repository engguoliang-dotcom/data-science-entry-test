def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    index = 0
    # Loop through the list as long as the index is within bounds
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]  # Return the first negative number immediately
        index += 1  # Move to the next element
        
    return "No negatives"  # Default return if the loop finishes without finding a negative


# Task 2
# Invoke the function "find_first_negative" using the provided scenarios:
list_1 = [3, 5, -1, 7, -2, 8]
list_2 = [2, 10, 7, 0]

result_1 = find_first_negative(list_1)
result_2 = find_first_negative(list_2)

print(f"First negative in {list_1}: {result_1}")  # Expected: -1
print(f"First negative in {list_2}: {result_2}")  # Expected: No negatives
