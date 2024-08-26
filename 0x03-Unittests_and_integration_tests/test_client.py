#!/usr/bin/env python3
"""Test client module for GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient  # Import the GithubOrgClient class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Patch get_json to prevent actual HTTP calls
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Parameters:
        org_name (str): The organization name to test.
        """
        # Setup the mock return value for get_json
        mock_get_json.return_value = {"org": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"org": org_name})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the expected URL.
        """
        # Create a mock GithubOrgClient with a mocked org property
        with patch('client.GithubOrgClient.org', return_value={"repos_url": "https://api.github.com/orgs/test/repos"}):
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', return_value="https://api.github.com/orgs/test/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that GithubOrgClient.public_repos
        returns the expected list of repos.

        Parameters:
        mock_public_repos_url: The mocked _public_repos_url property.
        mock_get_json: The mocked get_json function.
        """
        # Define the test payload
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload
        client = GithubOrgClient("test")
        repos = client.public_repos()
        # Ensure the property and get_json function were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
        self.assertEqual(repos, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license
        returns the correct result based on the license key.

        Parameters:
        repo (dict): The repository data with license information.
        license_key (str): The license key to check.
        expected (bool): The expected result of the license check.
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for the GithubOrgClient class using fixtures."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the patcher for requests.get to return predefined fixtures.
        """
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Configure side effects to return specific fixtures based on the URL
        cls.mock_get.side_effect = lambda url: Mock(json=lambda: cls._get_fixture(url))

    @classmethod
    def _get_fixture(cls, url):
        """
        Return the appropriate fixture based on the URL.
        Parameters:
        url (str): The URL being requested.
        """
        if url == "https://api.github.com/orgs/google":
            return cls.org_payload
        elif url == "https://api.github.com/orgs/test/repos":
            return cls.repos_payload
        elif url == "https://api.github.com/orgs/apache2/repos":
            return cls.apache2_repos
        return {}

    @classmethod
    def tearDownClass(cls):
        """
        Stop the patcher after tests are done.
        """
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """
        Integration test for
        GithubOrgClient.public_repos
        method using mocked HTTP calls.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)


if __name__ == "__main__":
    unittest.main()
