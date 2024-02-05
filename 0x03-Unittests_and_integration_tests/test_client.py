#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""


from client import *
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """
     Parameterize and patch as decorators
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """
        This method should test that GithubOrgClient.org returns
        the correct value.
        """
        mocked_fxn.return_value = MagicMock(return_value=resp)
        git_client = GithubOrgClient(org)
        self.assertEqual(git_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{org}".format(org)
        )
