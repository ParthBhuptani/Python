#Mini Assignment Write a palindrome checker: given a word, print whether it reads the same forwards and backwards (ignore case).

# Takes the input and convert it to lowercase(to ignore case)
s = input("Enter the string: ").lower()

# Check if the string is the same as its reverse using the slice operator
if s == s[::-1]:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")
