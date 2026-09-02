import string
import random

'''print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.ascii_letters.isascii)'''

rps = {1: "Rock", 2:"Paper", 3:"Scissors"}
#print(random.choice(rps.keys()))
'''print(random.choice(list(rps.values())))
print(rps[1])'''

comp_response = rps[random.choice([1, 2, 3])]
print(comp_response)