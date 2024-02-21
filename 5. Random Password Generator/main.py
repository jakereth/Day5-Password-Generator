import random

#create list of all characters that could be used
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?']

#get user inputs for each character amount
print("Welcome to the random password generator! This will implement letters(upper & lowercase), numbers and symbols.")
numLetters = int(input("How many letters would you like in the password? Enter a # "))
numNumbers = int(input("How many numbers would you like in the password? Enter a # "))
numSymbols = int(input("How many symbols would you like in the password? Enter a # "))

password = ''

#loop for each character choice 
for i in range(numLetters): 
        letChoice = random.randint(0, len(letters) - 1)
        password += letters[letChoice]
for n in range(numNumbers):
        numChoice = random.randint(0, len(numbers) - 1)
        password += numbers[numChoice]
for f in range(numSymbols):
        symChoice = random.randint(0, len(symbols) - 1)
        password += symbols[symChoice]
# Convert password to list for shuffling
password_list = list(password)
random.shuffle(password_list)

# Convert list back to string
password = ''.join(password_list)

print(f"Your password is:   {password}")