import unittest
import script

class TestScript(unittest.TestCase):
    def setUp(self):
        self.answer = 5
        
    def test_equal(self):
        guess = 5
        result = script.check_input(guess, self.answer)
        self.assertTrue(result)
        
    def test_wrong_answer(self):
        guess = 0
        result = script.check_input(guess, self.answer)
        self.assertFalse(result)
        
    def test_wrong_answer2(self):
        guess = 11
        result = script.check_input(guess, self.answer)
        self.assertFalse(result)
        
        
if __name__ == "__main__":
   unittest.main()