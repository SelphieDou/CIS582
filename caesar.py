

def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    for character in plaintext:
        num = ord(character)
        new_num = num + key
        if new_num > 90:
            new_num -= 26
        ciphertext += chr(new_num)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    for character in ciphertext:
        num = ord(character)
        new_num = num - key
        if new_num < 65:
            new_num += 26
        plaintext += chr(new_num)
    return plaintext

