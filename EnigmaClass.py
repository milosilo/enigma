
from colorama import init
from termcolor import colored
import random
import string
import time

class Enigma:
    def __init__(self):
        init()
        self.all_chars = string.printable
        self.rotors = [self.generate_rotor() for _ in range(3)]
        self.plugboard = self.create_plugboard([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H')])
    
    def generate_rotor(self):
        rotor = list(self.all_chars)
        random.shuffle(rotor)
        return ''.join(rotor)

    def rotate(self, rotor):
        return rotor[-1] + rotor[:-1]

    def transform_char(self, c, rotor):
        index = self.all_chars.index(c)
        return rotor[index]

    def transform_char_decode(self, c, rotor):
        index = rotor.index(c)
        return self.all_chars[index]

    def create_plugboard(self, swaps):
        plugboard = list(self.all_chars)
        for char1, char2 in swaps:
            index1, index2 = self.all_chars.index(char1), self.all_chars.index(char2)
            plugboard[index1], plugboard[index2] = plugboard[index2], plugboard[index1]
        return ''.join(plugboard)

    def apply_plugboard(self, c, plugboard):
        return plugboard[self.all_chars.index(c)]

    def encode(self, message):
        encoded_message = ""
        for i, c in enumerate(message):
            c = self.apply_plugboard(c, self.plugboard)
            active_rotor = self.rotors[i % len(self.rotors)]
            c = self.transform_char(c, active_rotor)
            self.rotors[i % len(self.rotors)] = self.rotate(active_rotor)
            c = self.apply_plugboard(c, self.plugboard)
            encoded_message += c
        return encoded_message

    def decode(self, encoded_message):
        decoded_message = ""
        for i, c in enumerate(encoded_message):
            c = self.apply_plugboard(c, self.plugboard)
            active_rotor = self.rotors[i % len(self.rotors)]
            c = self.transform_char_decode(c, active_rotor)
            self.rotors[i % len(self.rotors)] = self.rotate(active_rotor)
            c = self.apply_plugboard(c, self.plugboard)
            decoded_message += c
        return decoded_message
