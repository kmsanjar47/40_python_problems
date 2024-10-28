# Using list comprehension to create a new list with elements that meet a condition.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]

print('Even Numbers:', even_numbers)
