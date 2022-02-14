import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to test a function")
        
    def test_sum(self):
        test_param = 10
        result = main.sum(test_param)
        self.assertEqual(result, 15)
        
    def test_sum2(self):
        test_param = "abc"
        result = main.sum(test_param)
        self.assertEqual(result, "Please, enter a number!")
        
    def test_sum3(self):
        test_param = None
        result = main.sum(test_param)
        self.assertEqual(result, "Please, enter a number!")
    
    def test_sum4(self):
        test_param = ''
        result = main.sum(test_param)
        self.assertEqual(result, "Please, enter a number!")
    
    def tearDown(self):
        print("cleaning up")
        
        
if __name__ == "__main__":
   unittest.main()
