# -*- coding: utf-8 -*-

"""
Bitbucket repository processor
------------------------------
"""


from __future__ import unicode_literals

import httplib
import ssl
import json
import os
import base64

from pybitbucket.bitbucket import Client
from pybitbucket.auth import BasicAuthenticator
from pybitbucket.snippet import Snippet

from .repotools import RepoTools
from .exceptions import RepocloneException

class BitbucketRepo:
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

    def process_repo(self, clone_dir):
        data = self._get_repository_data()

        print(data)

    def _get_repository_data(self):
        print("Getting repository info from " + self.host + " ...")

        data = None
        try:
            bitbucket = Client(
                BasicAuthenticator(
                    'your_username_here',
                    'your_secret_password_here',
                    'pybitbucket@mailinator.com'))

            for snip in Snippet.find_snippets_for_role(client=bitbucket):
                print(snip)

        except Exception as e:
            print("\nGet repository data error: " + str(e))
            raise e

        return data
