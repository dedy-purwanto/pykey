import os
import unittest
import ConfigParser

from pykey import pykey

class TestMixin(object):

    def setUp(self):
        if os.path.isfile(pykey.CONFIG_FILENAME):
            os.remove(pykey.CONFIG_FILENAME)

    def cleanUp(self):
        if os.path.isfile(pykey.CONFIG_FILENAME):
            os.remove(pykey.CONFIG_FILENAME)

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

class TestConfig(TestMixin, unittest.TestCase):

    def test_write_config(self):
        old_config = pykey.get_config()
        new_config = pykey.write_config(old_config)
        self.assertTrue(isinstance(new_config, ConfigParser.RawConfigParser))

    def test_edit_config(self):
        old_config = pykey.get_config()
        old_config.add_section('main')
        old_config.set('main', 'vault', 'default.json')
        old_config.set('main', 'key', 'default.key')
        pykey.write_config(old_config)

        new_config = pykey.get_config()
        self.assertTrue(new_config.has_section('main'))
        self.assertEqual(new_config.get('main', 'vault'), 'default.json')
        self.assertEqual(new_config.get('main', 'key'), 'default.key')

    def test_get_config(self):
        config = pykey.get_config()
        self.assertTrue(isinstance(config, ConfigParser.RawConfigParser))

    def test_config_has_no_default(self):
        config = pykey.get_config()
        self.assertFalse(pykey.config_has_default(config))

    def test_config_has_default(self):
        old_config = pykey.get_config()
        old_config.add_section('main')
        old_config.set('main', 'vault', 'default.json')
        old_config.set('main', 'key', 'default.key')
        pykey.write_config(old_config)
        config = pykey.get_config()
        self.assertTrue(pykey.config_has_default(config))

if __name__ == '__main__':
    unittest.main()
