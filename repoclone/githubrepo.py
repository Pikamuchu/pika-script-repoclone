# -*- coding: utf-8 -*-

"""
Github repository processor
----------------------------
"""


from __future__ import unicode_literals

from git import Repo
from github import Github

from .repotools import RepoTools
from .exceptions import RepocloneException

class GithubRepo:
    """
    Process repo

    :param user: Repository credential user name.
    :param password: Repository credential password.
    """
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def process_repo(self, clone_dir):
        repos = self._get_repository_data()

        print("Processing github repo data ...")
        for repo in repos:
            repo_name = repo.name
            print("\nProcessing repo " + repo_name)

            # Creating project folder
            project_folder = self._create_project_folder(repo, clone_dir)

            # Determining ssh clone url
            repo_clone_url = self._get_repo_ssh_clone_url(repo)

            # Cloning repository
            RepoTools.clone_update_repository(repo_clone_url, project_folder, repo_name)

        return 0

    def _get_repository_data(self):
        print("Getting repository info from " + self.host + " ...")

        data = None
        try:
            g = Github(self.user, self.password)

            data = g.get_user(self.user).get_repos()
        except Exception as e:
            print("\nGet repository data error: " + str(e))
            raise e

        return data

    def _create_project_folder(self, repo, clone_dir):
        if repo.fork:
            return RepoTools.create_project_folder("forks", clone_dir)
        else:
            return RepoTools.create_project_folder(self.user, clone_dir)

    def _get_repo_ssh_clone_url(self, repo):
        return repo.git_url

