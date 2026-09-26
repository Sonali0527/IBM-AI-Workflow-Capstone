import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.discover('.', pattern='test_*.py'))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\nALL UNIT TESTS PASSED - Ready for peer review!")
    else:
        print("\nSome tests failed")
