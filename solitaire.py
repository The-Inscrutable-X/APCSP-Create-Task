import numpy as np
import random

#Variables
s_deck = []
s_new_deck = []
s_chars = []

#Variables based on input
s_type = str(input("Decrypt or encrypt, d/e: "))
s_seed = int(input("Input a deck order, can be any integer: "))

#Seed based on variable input
random.seed(s_seed)

#Additional message if encrypting
if str(s_type) == "e":
  print("Messages may only contain letters and spaces.")

#Variables based on input
s_string = str(input("Input a message to encrypt or decrypt: "))

#Makes string be only uppercase letters
s_string = ''.join(i for i in s_string if i.isalnum())
s_string = ''.join([i for i in s_string if not i.isdigit()])
s_string = s_string.upper()

#Encrypt
if s_type == "e":

  #Adds numbers from 1 to range number
  for i in range(54):
    s_add = i + 1
    s_deck.append(s_add)

  #Randomly shuffles deck into new deck
  for i in range(len(s_deck)):

    #Sets seed to previous random number
    s_rn = random.random()
    random.seed(s_rn)

    #Gets random integer based on seed
    s_take = random.randint(0, len(s_deck)-1)
    #Moves that card to new deck
    s_new_deck.append(s_deck[s_take])
    s_deck.pop(s_take)

  #Converts letters into numbers
  for i in s_string:
    s_chars.append(ord(i) - 64)

  #Shifts 53 one to right
  for i in range(len(s_new_deck)):
    if str(s_new_deck[i]) == "53":
      if i == 53:
        s_new_deck.insert(1, "53")
        s_new_deck.pop()

      else:
        s_new_deck.insert(i+2, "53")
        s_new_deck.pop(i)
  #Shifts 52 two to right
  for i in range(len(s_new_deck)):        
    if str(s_new_deck[i]) == "54":
      if i == 52:
        s_new_deck.insert(1, "54")
        s_new_deck.pop(52)
      if i == 53:
        s_new_deck.insert(2, "54")
        s_new_deck.pop()        
      if i < 52:
        s_new_deck.insert(i+3, "54")
        s_new_deck.pop(i)

  s_new_deck_1 = []
  s_new_deck_2 = []
  s_new_deck_3 = []

  s_53 = 2
  s_54 = 3
  
  for i in range(len(s_new_deck)):
    print(s_new_deck)
    if str(s_new_deck[i]) == "53":
      s_53 = i
  for i in range(len(s_new_deck)):
    if str(s_new_deck[i]) == "54":
      s_54 = i

  print(s_53)
  print(s_54)
  
  if s_54 > s_53:
    for i in range(s_53):
      s_new_deck_1.append(s_new_deck[i])
    for i in range(s_54, 53):
      s_new_deck_3.append(s_new_deck[i])
    for i in range(s_53, s_54+1):
      s_new_deck_2.append(s_new_deck[i])

  if s_54 < s_53:
    for i in range(s_54):
      s_new_deck_1.append(s_new_deck[i])
    for i in range(s_53, 53):
      s_new_deck_3.append(s_new_deck[i])
    for i in range(s_54, s_53+1):
      s_new_deck_2.append(s_new_deck[i])

print(s_new_deck_1)
print(s_new_deck_2)
print(s_new_deck_2)

if s_new_deck[53] == 53 or 

horse = [1, 2, 3]

horse.insert(2, "horse[1]")
print(horse)