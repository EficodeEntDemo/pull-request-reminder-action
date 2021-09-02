#!/usr/bin/env python
# Copyright - Eficode Oy - 2021 - All rights reserved

import unittest
import os
import main


class TestCode(unittest.TestCase):

    def test_should_pass(self):
        os.environ["GITHUB_REPOSITORY"] = "some-repo-name"
        os.environ["GITHUB_SERVER_URL"] = "some-server-url"
        main.main()
        #self.assertEqual(True, True)
