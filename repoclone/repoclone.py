# -*- coding: utf-8 -*-

"""
Main entry point for the `repoclone` command.

The code in this module is also a good example of how to use repoclone as a
library rather than a script.
"""


from __future__ import unicode_literals

import httplib
import ssl
import json
import os
import base64
import re

from .exceptions import RepocloneException
from .bitbucketrepo import BitbucketRepo
from .bitbucketprivaterepo import BitbucketPrivateRepo
from .githubrepo import GithubRepo

GITHUB_REPO_REGEX = r".*github\.com"

BITBUCKET_REPO_REGEX = r".*bitbucket\.org"

BITBUCKET_PRIVATE_REPO_REGEX = r".*bitbucket.*"

REPOS_CLONE_FOLDER = "./repos"

def repoclone(host=None, user=None, password=None, clone_dir=REPOS_CLONE_FOLDER):
    """
    Run repoclone just as if using it from the command line.

    :param host: Repository server host name.
    :param user: Repository credential user name.
    :param password: Repository credential password.
    :param clone_dir: Repository clone directory.
    :param endpoint: Repository info REST endpoint.
    """
    # Validating params
    if host is None:
        print("host parameter is requiered!")
        return 2

    if clone_dir is None:
        clone_dir = REPOS_CLONE_FOLDER

    if not re.match(GITHUB_REPO_REGEX, host) is None:
        print("Processing Github repo!")
        github = GithubRepo(host, user, password)
        github.process_repo(clone_dir)

    elif not re.match(BITBUCKET_REPO_REGEX, host) is None:
        print("Processing Bitbucket repo!")
        bitbucket = BitbucketRepo(host, user, password)
        bitbucket.process_repo(clone_dir)

    elif not re.match(BITBUCKET_PRIVATE_REPO_REGEX, host) is None:
        print("Processing Bitbucket private repo!")
        bitbucket = BitbucketPrivateRepo(host, user, password)
        bitbucket.process_repo(clone_dir)

    else:
        print("Unknown repository type!!")
        return 2

    return 0

