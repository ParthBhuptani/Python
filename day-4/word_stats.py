# Coding Task Write word_stats.py that takes a sentence as input and prints: number of characters, number of words, and the sentence in all uppercase.

# Takes the input
s = input("Enter the sentence:")

# len() -> returns length of string
print(len(s))

# split() -> breaks sentence into words, len() → counts them
print(len(s.split()))

# upper() -> returns string to uppercase
print(s.upper())
