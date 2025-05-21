# @Doctor Solo

from random import SystemRandom
from string import ascii_letters
from string import digits
from string import punctuation

class Password_Generator:
    def __init__(self, lenght:int, hasCharacter:bool=True):
        self.__lenght:int  = lenght
        self.__hasCharacter:bool = hasCharacter
    
    
    def Generator(self) -> str:
        __characters = ascii_letters + digits
        if self.__hasCharacter:
            __characters += punctuation
        
        return "".join(
            SystemRandom()
            .choice(__characters) for _ in range(self.__lenght)
            )
    
