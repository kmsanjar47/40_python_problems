# Generating a list of random numbers using random.randint().

import random
random_numbers = [random.randint(1, 100) for _ in range(5)]

print('Random Numbers:', random_numbers)
