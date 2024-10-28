# Flattening a nested list using a list comprehension.

nested_list = [[1, 2, 3], [4, 5], [6]]
flattened = [item for sublist in nested_list for item in sublist]

print('Flattened List:', flattened)
