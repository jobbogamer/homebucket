
# Standard library
import json

# 3rd party
import requests

# Local
from model.database import Repo

def get_repos_for_user(username):
    repos = make_request("users/{0}/repos".format(username))
    
    if repos is None:
        return None

    else:
        repo_objects = []
        for repo in repos:
            repo_object = Repo()

            repo_object.name = repo['name']
            repo_object.url = repo['html_url']
            repo_object.site_url = repo['homepage']
            repo_object.description = repo['description']

            repo_objects.append(repo_object)

        return repo_objects


def make_request(endpoint):
    url = "https://api.github.com/{0}".format(endpoint)
    response = requests.get(url)
    if (response.ok):
        result = json.loads(response.text or response.content)
        return result
    else:
        return None
