import random, string

MIN_LENGTH = 8
MAX_LENGTH = 40

class PasswordGenerator:
    @staticmethod
    def generate(length, characters):
        return ''.join(random.choice(characters) for _ in range(length))
    
class CharacterSet:
    @staticmethod
    def all():
        return string.ascii_letters + string.punctuation + string.digits
    
class PasswordGeneratorSevice:
    
    @staticmethod
    def generate(length:int=MIN_LENGTH,include_upper:bool=False, include_lower:bool=False, include_digits:bool=False, include_symbols:bool=False):
        characters = ''
        if include_upper:
            characters += string.ascii_uppercase
        if include_lower:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        return PasswordGenerator.generate(length,characters)

    @classmethod
    def generate_random_length_password(cls,upp:bool,low:bool,dig:bool,sym:bool):
        return cls.generate(length=random.randint(MIN_LENGTH, MAX_LENGTH),include_upper=upp,include_lower=low,include_digits=dig,include_symbols=sym)

    @staticmethod
    def generate_random_length_password_with_all_characters():
        return PasswordGenerator.generate(random.randint(MIN_LENGTH, MAX_LENGTH),CharacterSet.all())
    

a = PasswordGeneratorSevice.generate(8,True,False,False,True)
b = PasswordGeneratorSevice.generate_random_length_password(False, True, True, False)
c = PasswordGeneratorSevice.generate_random_length_password_with_all_characters()
print(f'{a}\n{b}\n{c}')
"""


tsmi6i2s
grtopz7toq5
J;Vcg:y-zfE

evidentemente esto no esta terminado
"""
