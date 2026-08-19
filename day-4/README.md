## Day 4 — Strings and String Methods

**Learning Objectives**
- Slice and index strings
- Use common string methods
- Format strings with f-strings

**Theory**
Strings are sequences of characters, indexable with `[]` (starting at 0) and sliceable with `[start:stop:step]`. Strings are immutable — methods like `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, and `.join()` return *new* strings rather than modifying the original. f-strings (`f"{variable}"`) are the modern way to embed values into text.

**Hands-On Exercises**
1. Given `s = "Python Programming"`, print the first 6 characters, then the last 11.
2. Reverse `s` using slicing (`s[::-1]`).
3. Use `.split()` to break a sentence into a list of words.
4. Use `.join()` to combine a list of words back into a sentence.
5. Use `.replace()` to censor a word in a sentence.

**Coding Task**
Write `word_stats.py` that takes a sentence as input and prints: number of characters, number of words, and the sentence in all uppercase.

**Mini Assignment**
Write a palindrome checker: given a word, print whether it reads the same forwards and backwards (ignore case).

**Revision Questions**
1. Why are strings called "immutable"?
2. What does `s[::-1]` do?
3. What's the difference between `.split()` and `.join()`?
4. How do f-strings differ from regular string concatenation?

**End-of-Day Challenge**
Write a simple Caesar cipher: shift every letter in a word forward by 1 in the alphabet (e.g., "abc" → "bcd"), printing the encoded result. (Hint: look up `ord()` and `chr()`.)
