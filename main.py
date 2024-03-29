#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numLetters= int(input("How many letters would you like in your password?\n")) 
numSymbols = int(input("How many symbols would you like?\n"))
numNumbers = int(input("How many numbers would you like?\n"))

characters=[]

for i in range(numLetters):
  choice=random.randint(0,len(letters)-1)
  characters+=letters[choice]

for j in range(numSymbols):
  choice=random.randint(0,len(symbols)-1)
  characters+=symbols[choice]

for k in range(numNumbers):
  choice=random.randint(0,len(numbers)-1)
  characters+=numbers[choice]

password=""
while len(password)!=len(characters):
  choice=random.choice(characters)
  if choice not in password:
    password+=choice
  else:
    choice=""
  
print(f"Your password is: {password}")