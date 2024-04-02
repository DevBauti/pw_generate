import random, string

MIN_LENGTH = 6
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
    def generate(include_upper=False, include_lower=False, include_digits=False, include_symbols=False):
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
    def generate_random_password():
        return PasswordGenerator.generate(random.randint(MIN_LENGTH, MAX_LENGTH),CharacterSet.all())