import string

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

