#!/usr/bin/env python
# Copyright - Eficode Oy - 2021 - All rights reserved

import unittest
import os
import main


class TestCode(unittest.TestCase):

    def test_should_pass(self):
        self.assertEqual(True, True)

    # def test_retrieve_all_pull_requests(self):
    #     os.environ["INPUT_GITHUB_TOKEN"] = "yourtokenmustnotbehereinthecode"
    #     os.environ["GITHUB_API_URL"] = "https://api.github.com"
    #     os.environ["GITHUB_REPOSITORY_OWNER"] = "EficodeEntDemo"
    #     os.environ["GITHUB_REPOSITORY"] = "pluto-the-beginning"
    #
    #     main.main()
