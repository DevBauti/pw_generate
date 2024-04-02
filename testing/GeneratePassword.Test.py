
import unittest
from GeneratePassword import PasswordGeneratorSevice, MIN_LENGTH,MAX_LENGTH

class TestPasswordGeneratorService(unittest.TestCase):

    def test_generate_password(self):
        pw = PasswordGeneratorSevice.generate()
        self.assertTrue(pw)
        self.assertGreaterEqual(len(pw),MIN_LENGTH)

    def test_generate_random_length_password(self):
        pw = PasswordGeneratorSevice.generate_random_length_password()
        self.assertTrue(pw)
        self.assertGreaterEqual(len(pw),MIN_LENGTH)
        self.assertLessEqual(len(pw), MAX_LENGTH)

    def test_generate_random_length_password_with_all_characters(self):
        pw = PasswordGeneratorSevice.generate_random_length_password_with_all_characters()
        self.assertTrue(pw)
        self.assertGreaterEqual(len(pw),MIN_LENGTH)
        self.assertLessEqual(len(pw), MAX_LENGTH)

if __name__ == '__main__':
    unittest.main()


"""
esto se tiene que mejorar bastante mas...
"""