import unittest
class TestFloatValue(unittest.TestCase):
    def test_float_values(self):
        values = [
            (2.4, 2.4),
            (3.2, 3.2),
            (4.4, 4.4),
            (5.1, 5.1)
        ]

        for num, expected in values:
            with self.subTest(number=num):
                self.assertEqual(num, expected)
if __name__ == "__main__":
    unittest.main()

