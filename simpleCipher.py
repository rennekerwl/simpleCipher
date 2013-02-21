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

def generate_ciphertext(message, key):
    cipherText = ''
    for letter in message:
        cipherText += key[letter]

    return cipherText

def load_cipher(cipherFile):
    cFile = open(cipherFile, 'r')
    cipher = file.read()
    cFile.close()
    return cipher

def save_cipher(cipherText):
    cipherFile = open('ciphertext.txt', 'w')
    cipherFile.write(cipherText)
    cipherFile.close()

def decode_cipher(cipherText, key):
    clearText = ''
    for letter in cipherText:
        clearText += find_key(key, letter)

    return clearText


def main():
    while True:
        eOrD = input('(E)ncrypt or (D)ecrypt or (Q)uit?')
        if eOrD == 'E':
            genOrNot = input('(G)enerate a key or (L)oad key?')
            if genOrLoad == 'G':
                message = get_message()
                key = generate_key(message)
                ciphertext = generate_ciphertext(message, key)
                print('Ciphertext:')
                print(ciphertext)
                saveOrNot = input('(S)ave a copy of the key & ciphertext or (N)ot?')
                if saveOrNot == 'S':
                    save_key(key)
                    save_cipher(ciphertext)
            elif genOrLoad == 'L':
                message = get_message()
                keyFile = input('Filename of key?')
                key = load_key(keyFile)
                ciphertext = generate_ciphertext(message, key)
                saveOrNot = input('(S)ave a copy of the ciphertext or (N)ot?')
                if saveOrNot == 'S':
                    save_cipher(ciphertext)
        if eOrD == 'D':
            cipherByHandOrLoad = input('(T)ype ciphertext by hand or (L)oad it?')
            if cipherByHandOrLoad == 'T':
                cipherText = input('Ciphertext: ')
                keyByHandOrLoad = input('(T)ype in key by hand or (L)oad it?')
                if keyByHandOrLoad == 'T':
                    key = input('Key: ')
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
                elif keyByHandOrLoad == 'L':
                    keyFile = input('What is the name of the key file?')
                    key = read_key(keyFile)
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
            elif cipherByHandOrLoad == 'L':
                cipherFile = input('What is the name of the ciphertext file?')
                keyByHandOrLoad = input('(T)ype in key by hand or (L)oad it?')
                if keyByHandOrLoad == 'T':
                    key = input('Key: ')
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
                elif keyByHandOrLoad == 'L':
                    keyFile = input('What is the name of the key file?')
                    key = read_key(keyFile)
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
        elif eOrD == 'Q':
            sys.exit()
        else:
            print('Not a valid choice')

if __name__ == '__main__':
    main()
