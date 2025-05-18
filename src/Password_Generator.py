from random import SystemRandom
from string import ascii_letters
from string import digits
from string import punctuation

class Password_Generator:
    def __init__(self, lenght:int, hasCharacter:bool=True):
        self.lenght = lenght
        self.hasCharacter = hasCharacter
    
    
    def Generator(self):
        characters = ascii_letters + digits
        if self.hasCharacter:
            characters += punctuation
        
        return "".join(SystemRandom().choice(characters) for _ in range(self.lenght))