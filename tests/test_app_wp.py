#!/usr/local/bin/python3 


import unittest
import argparse
from configparser import ConfigParser

# import app_wp

class TestAppWp(unittest.TestCase):
    
    def setUp(self):
        self.file = '/Users/spencer.anderson/dev/pythonshenanigans/flaskapi_crud/wp-creds'
        config = ConfigParser()
        username = config.get('wp'
        passwd = config.get('wp','passwd')


    def test_get_conf(self):
        self.assertEqual(self.username, 'correando')
        self.assertEqual(self.passwd, 'my56Busta*')


    # def test_format_creds(self):
    #     self.assertEqual('correando:my56Busta*')
    #     self.

if __name__ == '__main__':
    unittest.main()