import numpy as np
import random
s_seed = int(input("Input a deck order, can be any integer: "))

s_deck = []
s_new_deck = []

for i in range(4):
  s_add = i + 1
  s_deck.append(s_add)

for i in range(len(s_deck)):
  s_take = random.randint(0, len(s_deck)-1)
  s_new_deck.append(s_deck[s_take])
  s_deck.pop(s_take)

print(s_new_deck)