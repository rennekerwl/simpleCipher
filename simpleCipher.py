import random
import string

def find_key(dic, val):
    return [k for k, v in dic.items() if v == val][0]

def get_message():
    message = input('Message: ')
    
    return message
        
def generate_key():
    scrambled = ''
    alphabet = []
    key = {}
    for letter in string.ascii_letters[:26]:
        alphabet.append(letter)

    for x in range(26):
        letter = random.choice(alphabet)
        alphabet.remove(letter)
        scrambled += letter
        
    alphabet = string.ascii_letters[:26]

    for x in range(26):
        key[alphabet[x]] = scrambled[x]

    return key

def save_key(key):
    keyFile = open('key.txt', 'w')
    keyFile.write(key)
    keyFile.close()

def read_key(keyFile):
    file = open(keyFile, 'w')
    key = file.read()
    file.close()
    
    return key

def encode_cipher(message, key):
    cipherText = ''
    for letter in message:
        cipherText += key[letter]

    return cipherText

def save_cipher(cipherText):
    cipherFile = open('ciphertext.txt', 'w')
    cipherFile.write(cipherText)
    cipherFile.close()

def decode_cipher(cipherText, key):
    clearText = ''
    for letter in cipherText:
        clearText += find_key(key, letter)

    return clearText

