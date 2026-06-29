def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists in the dictionary
    if key in dct:
        print(f"Original value for key '{key}': {dct[key]}")
    
    # Update or insert the key-value pair
    dct[key] = value
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the provided scenarios:

# Scenario 1: Key does not exist
dict1 = {}
print("Scenario 1: Adding 'name': 'Alice' to empty dict")
result1 = update_dictionary(dict1, "name", "Alice")
print("Resulting Dictionary:", result1)

print("-" * 30)

# Scenario 2: Key already exists
dict2 = {"age": 25}
print("Scenario 2: Updating 'age' from 25 to 26")
result2 = update_dictionary(dict2, "age", 26)
print("Resulting Dictionary:", result2)
