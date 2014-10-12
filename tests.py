import unittest
import ConfigParser

from pykey import pykey

class TestVault(unittest.TestCase):

    def test_list_vault(self):
        self.assertTrue(False)

    def test_create_vault(self):
        self.assertTrue(False)

    def test_edit_vault(self):
        self.assertTrue(False)

class TestPassword(unittest.TestCase):

    def test_list_password(self):
        self.assertTrue(False)

    def test_find_password(self):
        self.assertTrue(False)

    def test_create_password(self):
        self.assertTrue(False)

    def test_edit_password(self):
        self.assertTrue(False)

    def test_get_password(self):
        self.assertTrue(False)

class TestConfig(unittest.TestCase):

    def test_open_config(self):
        self.assertTrue(False)
    def test_write_config(self):
        old_config = pykey.get_config()
        new_config = pykey.write_config(old_config)
        self.assertTrue(isinstance(new_config, ConfigParser.RawConfigParser))

    def test_edit_config(self):
        self.assertTrue(False)

    def test_create_config(self):
        self.assertTrue(False)
    def test_get_config(self):
        config = pykey.get_config()
        self.assertTrue(isinstance(config, ConfigParser.RawConfigParser))

if __name__ == '__main__':
    unittest.main()
