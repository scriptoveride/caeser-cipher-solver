import string

shift = 0
words = ["was", "that", "with", "this", "cipher", "hello", "and", "test", ]  # Common words for the program to look out for 

text = input("Enter your cipher: ")
text = text.lower()
print("\n")
for i in range(26):
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted = text.translate(table)
    if any(word in encrypted.lower() for word in words):
        print(shift, " ", encrypted, "      POSSIBLE ANSWER")
        shift += 1
    else:
        print(shift, " ", encrypted)
        shift += 1
