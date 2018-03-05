"""
Robert Matthews
CS 1400
Section 002
Exercise 5

5.2
Give an example of a substitution cipher.
"""

"""
set alphabet, key, and text to encrypt and decrypt
alphabet = "abcdefghijklmnopqrstuvwxyz.,! ?"
key = ".,!python abcdefgijklmqrsuvwxz?"
"""

# below I have either a pause for user input, or a segment of a test message
message = str(input("What text would you like to encrypt? "))
message = message.lower()
# message = "hello, this is pretty cool!"

# turned my alphabet and key into a structured list--e for encrypt and d for decrypt
encrypt_key = {'a': '.', 'b': ',', 'c': '!', 'd': 'p', 'e': 'y', 'f': 't', 'g': 'h', 'h': 'o', 'i': 'n', 'j': ' ',
               'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'i', 's': 'j', 't': 'k',
               'u': 'l', 'v': 'm', 'w': 'q', 'x': 'r', 'y': 's', 'z': 'u', ',': 'v', '.': 'w', '!': 'x', ' ': 'z',
               '?': '?'}
# it looked really even until I wanted to add a question mark in...

decrypt_key = dict((e, d) for d, e in encrypt_key.items())
# assign functions for encrypt and decrypt


def encrypt(a_message):
    encrypted = ""
    # have the loop go through one character at a time and convert/encrypt. After the loop is done, add the encrypted
    # character and start over on the next character
    for character in a_message:
        value = encrypt_key[character]
        encrypted = encrypted + value

    return encrypted


def decrypt(a_message):

    decrypted = ""

    for character in a_message:
        value = decrypt_key[character]
        decrypted = decrypted + value

    return decrypted


print("Original message:\t", message)
encrypted_message = encrypt(message)
print("Encrypted message:\t", encrypted_message)
decrypted_message = decrypt(encrypted_message)
print("Decrypted message:\t", decrypted_message)

# the real downside to this cipher is that it doesn't read uppercase letters, and that it does not include more symbols
# I wanted to make it more in depth by having it add a space/symbol every few characters that the decryption function
# would remove
