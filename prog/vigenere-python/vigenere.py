#! /usr/bin/env python3
# coding: utf-8

'''
Handles upper case only
'''
class Vigenere:
    def __init__(self, key):
        self.key = key
    def encrypt(self, s):
        return self.compute(s, 'encrypt')
    def decrypt(self, s):
        return self.compute(s, 'decrypt')
    def compute(self, s, operation):
        result = ''
        keyIndex = 0
        for char in s:
            charAscii = ord(char)
            if not char.isupper():
                result += char
                continue
            # get offset
            keyChar = self.key[keyIndex]
            keyAscii = ord(keyChar)
            if operation == 'encrypt':
                offset = (charAscii + keyAscii) % 26
            else:
                offset = (charAscii - keyAscii) % 26
            # get letter
            result += chr(ord('A')+offset)
            # update key index
            keyIndex = (keyIndex+1) % len(self.key)
        return result
