# -*- coding: utf-8 -*-

"""
Repository tools
----------------
"""


from __future__ import unicode_literals

import os

from git import Repo

class RepoTools:
    """
    Repo tools

    """
    @classmethod
    def create_project_folder(self, project_dir, clone_dir):
        project_folder = clone_dir + "/" + project_dir
        if not os.path.exists(project_folder):
            print("Creating project folder " + project_folder)
            os.makedirs(project_folder)

        return project_folder

    @classmethod
    def clone_update_repository(cls, repo_clone_url, project_folder, repo_name):
        try:
            if repo_clone_url is not None:
                repo_clone_dir = project_folder + "/" + repo_name
                if not os.path.exists(repo_clone_dir):
                    print("Cloning repo " + repo_clone_url + " into " + repo_clone_dir)
                    Repo.clone_from(repo_clone_url, repo_clone_dir)
                else:
                    if os.path.isdir(repo_clone_dir + "/.git"):
                        print("Repo " + repo_clone_url + " already cloned! Pulling changes!!")
                        repo = Repo(repo_clone_dir)
                        origin = repo.remotes.origin
                        origin.pull()
                    else:
                        print("Repo directory " + repo_clone_url + " exists, but not a git repository???!!!???")
        except Exception as e:
            print("Clone update repository error: " + str(e))
            return 1

        return 0
