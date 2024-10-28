# Creating a dictionary with dictionary comprehension.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = {k: v for k, v in zip(keys, values)}
print('Dictionary:', my_dict)
