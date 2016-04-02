#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from zlasker import app
import unittest
import tempfile


class ZlaskerTestCase(unittest.TestCase):

    def setUp(self):
        self.bd_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.init_db()

    def tearDown(self):
        os.close(self.bd_fd)
        os.unlink(app.config['DATABASE'])

    # TODO: unit-testing

if __name__ == '__main__':
    unittest.main()
