import unittest
from translator.py import englishToFrench, frenchToEnglish

class Test_englishToFrench(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(englishToFrench(""), "")
    
    def testHelloInput(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class Test_frenchToEnglish(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(frenchToEnglish(""), "")
    
    def testHelloInput(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()