import random, string

MIN_LENGTH = 8
MAX_LENGTH = 30

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
    def generate(include_upper=False, include_lower=True, include_digits=True, include_symbols=False):
        characters = ''
        if include_upper:
            characters += string.ascii_uppercase
        if include_lower:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        return characters

    @classmethod
    def generate_password(cls):
        return PasswordGenerator.generate(MIN_LENGTH, cls.generate())
    
    @classmethod
    def generate_random_length_password(cls):
        return PasswordGenerator.generate(random.randint(MIN_LENGTH, MAX_LENGTH),cls.generate())

    @staticmethod
    def generate_random_length_password_with_all_characters():
        return PasswordGenerator.generate(random.randint(MIN_LENGTH, MAX_LENGTH),CharacterSet.all())
    

"""
a = PasswordGeneratorSevice.generate_password()
b = PasswordGeneratorSevice.generate_random_length_password()
c = PasswordGeneratorSevice.generate_random_length_password_with_all_characters()

print(f'{a}\n{b}\n{c}')

tsmi6i2s
grtopz7toq5
J;Vcg:y-zfE

evidentemente esto no esta terminado
"""