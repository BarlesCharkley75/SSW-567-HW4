# SSW567 HW5a
import unittest
import ssw567hw4a
from unittest import mock
from unittest.mock import patch
from ssw567hw4a import getCommits

class Test_ssw567hw4a(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ssw567hw4a.getCommits('BarlesCharkley75'), 168)
    
    @patch('ssw567hw4a.json.loads')

    def test_1(self, mocking):
        mocking.return_value.count = 168
        jay = ssw567hw4a.getCommits('BarlesCharkley75')
        self.assertEqual(jay, 0)
        
    def test_2(self):
        self.assertEqual(ssw567hw4a.getCommits(1234567),"User ID is not valid")

    @patch('ssw567hw4a.json.loads')

    def test_2(self, mocking):
        mocking.return_value.count = "User ID is not valid"
        jay = ssw567hw4a.getCommits(1234567)
        self.assertEqual(jay, "User ID is not valid")
        
if __name__ == '__main__':
    unittest.main()