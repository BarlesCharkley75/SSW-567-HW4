import unittest
import ssw567hw4a

class Test_ssw567hw4a(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ssw567hw4a.getCommits('BarlesCharkley75'), 146)
    def test_2(self):
        self.assertEqual(ssw567hw4a.getCommits(1234567),"User ID is not valid")
if __name__ == '__main__':
    unittest.main()