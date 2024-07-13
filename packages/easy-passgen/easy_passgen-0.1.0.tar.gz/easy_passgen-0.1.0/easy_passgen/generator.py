#!/usr/bin/env python3

import random
import string

class Generator():

    def __init__(self, length, use_symbols):

        self._length = length
        self._use_symbols = use_symbols

    @property
    def length(self):

        return self._length

    @length.setter
    def length(self, length):

        self._length = length

    @property
    def use_symbols(self):

        return self._use_symbols

    @use_symbols.setter
    def use_symbols(self, use_symbols):

        self._use_symbols = use_symbols

    def generate(self):

        chars = string.ascii_letters + '0123456789' 
        symbols = string.punctuation
        result = '' 

        if self.use_symbols:

            for i in range(self.length):
                
                result += random.choice(chars + symbols)
        else:

            for i in range(self.length):

                result += random.choice(chars)

        return result

    def generate_and_print(self):

        print(f"[+] Generated password: {self.generate()}")
