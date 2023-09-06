import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)



#Crypter un message

plain_text = input("Entrez une message à crypter: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"message original: {plain_text}")
print(f"message crypté: {cipher_text}")



#Décrypter un message

cipher_text = input("Entrez une message à décrypter: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"message crypté: {cipher_text}")
print(f"message original: {plain_text}")