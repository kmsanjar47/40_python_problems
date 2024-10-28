# Filtering even numbers from a list using filter().

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print('Even Numbers:', even_numbers)
