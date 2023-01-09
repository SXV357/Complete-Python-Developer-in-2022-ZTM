# phase 1 - reverse cypher
# phase 2 - caesar cypher

# read strings to encrypt from plainText.txt
# write encrypted strings to encryptedText.txt
# read strings from encryptedText.txt and decrypt them
# print decrypted strings to screen

# for encryption
# reverse string
# rotate each char in the string by 10 positions(moving forward from current position)


def encryption(txt):
    result = " "
    reversed = txt[::-1]
    for i in range(len(reversed)):
        char = reversed[i]
        if (char.isupper()):
            result += str(chr(char
                          ((ord(char) + 10 - 65) % 26 + 65)))
        else:
            result += str(chr(char
                          ((ord(char[i]) + 10 - 97) % 26 + 97)))

    return result


def decryption(txt):
    result = " "
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += str(chr((char((ord(char) - 10 + 65) % 26 + 65))))
        else:
            result += str(chr(char((ord(char) - 10 - 97) % 26 + 97)))

    return result[::-1]


print(encryption("Zoo"))
print(decryption("yyJ"))

# plain = open("plainText.txt", r)
# encrypted = open("encryptedText.txt", rw)

# for i in range(len(plain.readLines())):
    # encrypted.write(encryption(plain.readLine(i)))

# for j in range(len(encrypted.readLines())):
    #  print(decryption(encrypted.readLine(j)))
