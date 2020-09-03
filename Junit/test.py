import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

    def test_true(self):
        self.assertTrue( 5==5  , "should be true ")

    def test_false(self):
        self.assertFalse( 2==3,  "Should be false" )

    def test_Is(self):
            self.assertIs( type(5), int, "should be  innt")
if __name__ == '__main__':
    unittest.main()
