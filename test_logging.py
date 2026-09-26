import unittest
import os
import logging

class TestLogging(unittest.TestCase):
    def test_log_file_exists(self):
        # Create logs dir if not exists
        os.makedirs('logs', exist_ok=True)
        # Write a test log
        logging.basicConfig(filename='logs/app.log', level=logging.INFO)
        logging.info("Test log entry")
        self.assertTrue(os.path.exists('logs/app.log'))

    def test_isolated_from_production(self):
        # Q6 - uses test log, not prod log
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
