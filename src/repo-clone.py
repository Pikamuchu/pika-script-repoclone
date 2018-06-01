import httplib
import json
import os
from git import Repo

BITBUCKET_HOST = "bitbucket.desigual.com"
BITBUCKET_REPOS_ENDPOINT = "/rest/api/1.0/repos?limit=1000"

REPOS_CLONE_FOLDER = "./repos/"

# Get repository data
print "Getting repository data... "
conn = httplib.HTTPSConnection(BITBUCKET_HOST)
conn.request("GET", BITBUCKET_REPOS_ENDPOINT)
response = conn.getresponse()
data = json.loads(response.read())
conn.close()

# Processing response
print "Processing response ..."
repos = data["values"]
for repo in repos:
    repo_name = repo["slug"]
    print "Processing repo " + repo_name

    # Creating project folder
    project_folder = REPOS_CLONE_FOLDER + repo["project"]["key"]
    if not os.path.exists(project_folder):
        print "Creating project folder " + project_folder
        os.makedirs(project_folder)

    # Determining ssh clone url
    repo_clone = repo["links"]["clone"][0]
    repo_clone_url = repo_clone["href"]
    if not repo_clone["name"] is "ssh":
        repo_clone_url = repo["links"]["clone"][1]["href"]

    # Cloning repository
    if not repo_clone_url is None:
        repo_clone_dir = project_folder + "/" + repo_name
        print "Cloning repo " + repo_clone_url + " into " + repo_clone_dir
        Repo.clone_from(repo_clone_url, repo_clone_dir)

print "End"