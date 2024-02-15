# #!/usr/bin/env python3

from appconfig import app
INVALID_NUMBER = -1
# Implementation of hashid algorithm
class IdMapping():
    def __init__(self, salt='', max_num_len = 10, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'):
        self.salt = salt
        self.alphabet = self.shuffle_alphabet(alphabet, salt)
        self.max_num_len = max_num_len

    # Shuffles the alphabet based on the salt, providing a unique encoding/decoding sequence.
    def shuffle_alphabet(self, alphabet, salt):
        if not salt:
            return alphabet
        salt_chars = [ord(c) for c in salt]
        shuffled = list(alphabet)
        for i in range(len(shuffled)-1, 0, -1):
            j = salt_chars[i % len(salt_chars)] % (i+1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return ''.join(shuffled)

    # Encodes a given number into a hash string using the shuffled alphabet.
    def encode(self, number):
        if number == 0:
            return self.alphabet[0]

        encoded = ''
        alpha_len = len(self.alphabet)
        while number > 0:
            number, remainder = divmod(number, alpha_len)
            encoded = self.alphabet[remainder] + encoded

        return encoded

    # Decodes a given hash string back into a number using the shuffled alphabet.
    # Ensure return invalid number when catch exception or number overflow
    def decode(self, hash_str):
        try:
            number = 0
            alpha_len = len(self.alphabet)
            for char in hash_str:
                position = self.alphabet.index(char)
                number = number * alpha_len + position
            if len(str(number)) > self.max_num_len:
                return INVALID_NUMBER
        except ValueError:
            return INVALID_NUMBER
        return number

id_mapping = IdMapping(salt=app.config.get('SECRET_KEY'))
