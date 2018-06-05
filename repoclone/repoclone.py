# -*- coding: utf-8 -*-

"""
Main entry point for the `repoclone` command.

The code in this module is also a good example of how to use repoclone as a
library rather than a script.
"""

from __future__ import unicode_literals

import logging
import httplib
import ssl
import json
import os
import base64

from git import Repo

from .exceptions import (
    RepocloneException,
    RepositoryCloneFailed
)

BITBUCKET_HOST = "bitbucket.desigual.com"
BITBUCKET_REPOS_ENDPOINT = "/rest/api/1.0/repos?limit=1000"

REPOS_CLONE_FOLDER = "./repos"

def repoclone(
        type="BITBUCKET", host=BITBUCKET_HOST, user=None, password=None,
        clone_dir=REPOS_CLONE_FOLDER, endpoint=BITBUCKET_REPOS_ENDPOINT):
    """
    Run repoclone just as if using it from the command line.

    :param host: Repository server host name.
    :param user: Repository credential user name.
    :param password: Repository credential password.
    :param clone_dir: Repository clone directory.
    :param endpoint: Repository info REST endpoint.
    """
    # Validating params
    if clone_dir is None:
        clone_dir=REPOS_CLONE_FOLDER

    # Get repository data
    data = get_repository_data(host, endpoint, user, password)

    # Processing response
    print "Processing response ..."
    repos = data["values"]
    for repo in repos:
        repo_name = repo["slug"]
        print "Processing repo " + repo_name

        # Creating project folder
        project_folder = clone_dir + "/" + repo["project"]["key"]
        if not os.path.exists(project_folder):
            print "Creating project folder " + project_folder
            os.makedirs(project_folder)

        # Determining ssh clone url
        repo_clone = repo["links"]["clone"][0]
        repo_clone_url = repo_clone["href"]
        if not repo_clone["name"] == "ssh":
            repo_clone_url = repo["links"]["clone"][1]["href"]

        # Cloning repository
        if not repo_clone_url is None:
            repo_clone_dir = project_folder + "/" + repo_name
            if not os.path.exists(repo_clone_dir):
                print "Cloning repo " + repo_clone_url + " into " + repo_clone_dir
                Repo.clone_from(repo_clone_url, repo_clone_dir)
            else:
                if os.path.isdir(repo_clone_dir + "/.git"):
                    print "Repo " + repo_clone_url + " already cloned! Pulling changes!!"
                    repo = Repo(repo_clone_dir)
                    origin = repo.remotes.origin
                    origin.pull()
                else:
                    print "Repo directory " + repo_clone_url + " exists, but not a git repository???!!!???"

    return 0

def get_repository_data(host, endpoint, user, password):
    print "Getting repository info from " + host + " ..."
    conn = httplib.HTTPSConnection(host)
    conn._context.check_hostname = False
    conn._context.verify_mode = ssl.CERT_NONE
    headers = { "Authorization" : "Basic %s" % base64.standard_b64encode(user + ":" + password) }
    conn.request("GET", endpoint, headers=headers)
    response = conn.getresponse()
    data = None
    if response.status == 200:
        data = json.loads(response.read())
        conn.close()
    else:
        conn.close()
        raise RepositoryCloneFailed("Server " + host + " response with code " + str(response.status))

    return data
