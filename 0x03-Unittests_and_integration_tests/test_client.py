#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""


from client import *
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
     Parameterize and patch as decorators
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """
        This method should test that GithubOrgClient.org returns
        the correct value.
        """
        mocked_fxn.return_value = MagicMock(return_value=resp)
        git_client = GithubOrgClient(org)
        self.assertEqual(git_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """
         unit-tests GithubOrgClient._public_repos_url
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as f:
            f.return_value = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
        ({"license": {"key": "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
         unit-tests GithubOrgClient.has_license
        """
        git_client = GithubOrgClient("google")
        licensed_client = git_client.has_license(repo, key)
        self.assertEqual(licensed_client, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test: fixtures
    """
    def test_public_repos(self) -> None:
        """
         tests GithubOrgClient.public_repos
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self) -> None:
        """
        tests the public_repos with the argument license="apache-2.0"
        and make sure the result matches the expected value from the fixtures.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )
