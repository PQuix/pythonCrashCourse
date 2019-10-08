import unittest

import python_repos as pr

class RepoTestCase(unittest.TestCase):
    """Tests for 'python_repos.py'"""
    def setUp(self):
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_get_response(self):
        """Checks if response code is 200"""
        self.assertEqual(self.r.status_code, 200)
    
    def test_get_repo_dicts(self):
        """Checks if we get the anticipated data"""
        # We should get dicts for 30 repos
        self.assertEqual(len(self.repo_dicts), 30)

        # We should get the required keys
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

unittest.main()