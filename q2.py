def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Verify that the input is a list
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
        
    # Iterate through the list by index to modify it in place
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
            
    return lst


# Task 2
# Invoke the function "find_and_replace" using the provided scenarios:

# Scenario 1: Numeric list
list1 = [1, 2, 3, 4, 2, 2]
result1 = find_and_replace(list1, 2, 5)
print("Scenario 1 Result:", result1)

# Scenario 2: String list
list2 = ["apple", "banana", "apple"]
result2 = find_and_replace(list2, "apple", "orange")
print("Scenario 2 Result:", result2)
