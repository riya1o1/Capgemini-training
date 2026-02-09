import unittest
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(WidgetTestCase("test_default_width_size"))
    test_suite.addTest(WidgetTestCase("test_width_resize"))
    return test_suite
if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
