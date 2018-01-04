import unittest

def cal(a, b):
    return a+b

class CalTest1(unittest.TestCase):
    def testA(self):
        expected = 6
        result = cal(2, 4)
        self.assertEqual(expected, result)

    def testB(self):
        expected = 0
        result = cal(2, 1)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
