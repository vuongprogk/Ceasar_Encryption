ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(key, msg):
    ciphertext = ""
    for value in msg:
        if value in ALPHA:
            ciphertext += ALPHA[(ALPHA.find(value) + key) % len(ALPHA)]
        else:
            ciphertext += value
    return ciphertext


def decrypt(key, msg):
    plaintext = ""
    for value in msg:
        if value in ALPHA:
            plaintext += ALPHA[(ALPHA.find(value) - key) % len(ALPHA)]
        else:
            plaintext += value
    return plaintext
