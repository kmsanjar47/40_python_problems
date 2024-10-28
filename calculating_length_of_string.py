# Counting the number of vowels in a string.

text = "Python programming is fun!"
vowels = 'aeiou'
count = sum(1 for char in text.lower() if char in vowels)

print('Vowel Count:', count)
