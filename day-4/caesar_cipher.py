#End-of-Day Challenge Write a simple Caesar cipher: shift every letter in a word forward by 1 in the alphabet (e.g., "abc" → "bcd"), printing the encoded result. (Hint: look up ord() and chr().)

# Takes the input string
word = input("Enter the string: ")

# Stores the encoded string
result = ""

# Goes through each character in the string
for ch in word:
    code = ord(ch)  # Converts the character into its Unicode number
    new_ch = chr(code + 1) # Adds 1 to get the next character and converts it back to a character
    result += new_ch # Adds the new character to the result

# Prints the encoded string
print(result)


# ord() -> converts a character to its Unicode value
# chr() -> converts a Unicode value back to a character
