import string
import hashlib

alphabet = string.ascii_lowercase
key = 3
message = input("Enter a message: ")
encoded = ""

for letter in message:
    position = alphabet.find(letter)
    new_position = (position + key) % 26
    encoded = encoded + alphabet[new_position]

print("The encoded message is:", encoded)

decoded = ""

for letter in encoded:
    position = alphabet.find(letter)
    new_position = (position - key) % 26
    decoded = decoded + alphabet[new_position]

print("The decoded message is:", decoded)

# attempted solution at converting md5 hash to string
def md5hash_to_string(hsh):
    
    chars = {}
    for i in range(256):
        chars[chr(i)] = i

    
    hsh = [int(hsh[i:i+2], 16) for i in range(0, len(hsh), 2)]

    
    strings = []
    for i in range(256):
        for j in range(256):
            for k in range(256):
                for l in range(256):
                    for m in range(256):
                        string = chr(i) + chr(j) + chr(k) + chr(l) + chr(m)
                        strings.append(string)

    
    for string in strings:
        if hashlib.md5(string.encode()).hexdigest() == hsh:
            return string

    
    return None

