import string

alphabet = list(string.ascii_lowercase)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

word_dict = {}

for letter in alphabet:
    letter_count = 0
    for word in words:
        if letter in word.lower():
            letter_count += 1
        word_dict[letter] = letter_count

print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} found in the document\n")

for key, value, in word_dict.items():
    print(f"The {key} character was found {value} times")
print("--- End report ---")
