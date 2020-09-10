from sample import *
import unittest

#class TestType(unittest.TestCase):
#    def test_input_text(self):
#        self.assertRaises(TypeError, True)

class TestChoice(unittest.TestCase):
    def test_input_choice(self):
        a=['encode', 'decode']
        self.assertIn(choice, a)

if __name__ == '__main__':

    unittest.main()
