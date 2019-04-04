import os
from github import Github

_all_ = ['check_if_repo_exists']

def authenticate():
    try: 
        return Github(os.environ['GITHUB_USER'], os.environ['GITHUB_ACCESS_TOKEN'])
    except:
        return

def check_if_repo_exists(repos, new_repo_name):
    for r in repos:
            repo_name = r.full_name.split("/")[1]
            if repo_name == new_repo_name:
                return True
    return False

github = authenticate()
user = github.get_user()