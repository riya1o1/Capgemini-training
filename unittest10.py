import unittest
import sys
class mylib:
    __version__ = (1, 2)
def external_resource_available():
    return False  
class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in the library version")
    def test_format(self):
        self.assertTrue(True)
    @unittest.skipUnless(sys.platform.startswith("win"),
                         "windows-only test")
    def test_windows_support(self):
        self.assertTrue(True)

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        self.assertTrue(True)
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        self.assertTrue(True)
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, 'broken')
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{} doesn't have {}".format(obj, attr))
if __name__ == "__main__":
    unittest.main()

    