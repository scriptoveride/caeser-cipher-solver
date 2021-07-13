import string

shift = 0
words = ["was", "that", "with", "this", "cipher", "hello", "and", "test", ]  # Common words for the program to look out for 

print(
	'''
  _____                              _____ _       _                 _____                     _           
 / ____|   By scriptoveride         / ____(_)     | |               |  __ \                   | |          
| |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __  | |  | | ___  ___ ___   __| | ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__| | |  | |/ _ \/ __/ _ \ / _` |/ _ \ '__|
| |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |    | |__| |  __/ (_| (_) | (_| |  __/ |   
 \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|    |_____/ \___|\___\___/ \__,_|\___|_|   
                                            | |                                                            
                                            |_| 
 	'''
	)

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
