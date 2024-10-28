# Finding the most common element in a list using max() and count().

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
mode = max(set(numbers), key=numbers.count)

print('Mode:', mode)
