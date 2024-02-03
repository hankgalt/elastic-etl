import os
import unittest
from dotenv import load_dotenv
from utils.file import absolute_file_path

from creds import credentials

class TestFileUtils(unittest.TestCase):
    def test_print_env(self):
        print('\ntest_print_env() - ROOT_CERT_FILE: {}\n'.format(os.getenv('ROOT_CERT_FILE')))
        # assertions
        self.assertEqual(True, True, "should be equal")

    def test_absolute_path(self):
        filePath = "certs/server.pem"
        realPath = absolute_file_path(filePath)
        print('\ntest_absolute_path() - real path: {}\n'.format(realPath))
        # assertions
        self.assertEqual(True, filePath in realPath, "should be equal")

    def test_load_file(self):
        filePath = "certs/server.pem"
        realPath = credentials.load_file(filePath)
        print('\ntest_load_file() - real path: {}\n'.format(realPath))
        # assertions
        self.assertEqual(True, filePath in realPath, "should be equal")

    def test_load_file(self):
        SERVER_CERT_FILE = os.getenv('SERVER_CERT_FILE')
        SERVER_CERT = credentials.load_credential_from_file(SERVER_CERT_FILE)
        print('\ntest_load_file() - cert length: {}\n'.format(len(SERVER_CERT)))
        # assertions
        self.assertEqual(len(SERVER_CERT), 1529, "should be equal")

if __name__ == '__main__':
    load_dotenv("env/test.env")
    unittest.main()