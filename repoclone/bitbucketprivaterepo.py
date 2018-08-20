# -*- coding: utf-8 -*-

"""
Bitbucket private repository processor
--------------------------------------
"""


from __future__ import unicode_literals

import httplib
import ssl
import json
import os
import base64

from git import Repo

from .repotools import RepoTools
from .exceptions import RepocloneException

BITBUCKET_REPOS_ENDPOINT = "/rest/api/1.0/repos?limit=1000"

class BitbucketPrivateRepo:
    """
    Process repo

    :param host: Repository server host name.
    :param user: Repository credential user name.
    :param password: Repository credential password.
    """
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.endpoint = BITBUCKET_REPOS_ENDPOINT

    def process_repo(self, clone_dir):
        data = self._get_repository_data()

        print("Processing bitbucket repo ...")
        repos = data["values"]
        for repo in repos:
            repo_name = repo["slug"]
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
        conn = httplib.HTTPSConnection(self.host)
        conn._context.check_hostname = False
        conn._context.verify_mode = ssl.CERT_NONE

        data = None
        try:
            if self.user is None:
                conn.request("GET", self.endpoint)
            else:
                headers = {"Authorization" : "Basic %s" % base64.standard_b64encode(str(self.user) + ":" + str(self.password))}
                conn.request("GET", self.endpoint, headers=headers)

            response = conn.getresponse()

            if response.status == 200:
                data = json.loads(response.read())
            else:
                raise RepocloneException("Server " + self.host + " response with code " + str(response.status))

        except Exception as e:
            print("\nGet repository data error: " + str(e))
            raise e
        else:
            conn.close()

        return data

    def _create_project_folder(self, repo, clone_dir):
        return RepoTools.create_project_folder(repo["project"]["key"], clone_dir)

    def _get_repo_ssh_clone_url(self, repo):
        repo_clone = repo["links"]["clone"][0]
        repo_clone_url = repo_clone["href"]
        if not repo_clone["name"] == "ssh":
            repo_clone_url = repo["links"]["clone"][1]["href"]

        return repo_clone_url

