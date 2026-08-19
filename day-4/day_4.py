s = "Python Programming"

print(s[:6])          # Slicing: first 6 characters
print(s[7:])          # Slicing: from index 7 to the end
print(s[::-1])        # Slicing: reverse the string
print(len(s))         # len() -> returns the length of the string

for x in s:
    print(x, end="")  # Loops through each character; end="" keeps it on the same line

print("ram" in s)     # in -> checks if "ram" exists in the string
print("java" not in s) # not in -> checks if "java" does not exist

print(s[3])           # Indexing: gets character at index 3

print(s.upper())      # upper() -> converts string to uppercase
print(s.lower())      # lower() -> converts string to lowercase
print(s.lower())      # lower() -> converts string to lowercase

print(s.strip())      # strip() -> removes spaces from beginning and end

print(s.replace('P', 'J'))  # replace() -> replaces P with J

print(bool(0))        # bool(0) -> False

b = "Hello, World!"

print(b[-5:-2])       # Negative slicing: counts indexes from the end

print(s.split())      # split() -> breaks string into a list of words

print(s.join("--"))  # join() -> puts s between the characters of "--"
