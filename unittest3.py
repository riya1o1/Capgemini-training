import unittest
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass
    def test_strings_a(self):
        self.assertEqual('a'*4,'aaaa')
unittest.main()