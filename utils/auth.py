import os
from github import Github

def authenticate():
    try: 
        return Github(os.environ['GITHUB_USER'], os.environ['GITHUB_ACCESS_TOKEN'])
    except:
        return

def check_if_repo_exists(new_repo_name):
    for r in user.get_repos():
            repo_name = r.full_name.split("/")[1]
            if repo_name == new_repo_name:
                return True
    return False

def is_license_valid(license_key):
    for license in github.get_licenses():
        if license.key == license_key:
            return True
    return False

def is_gitignore_valid(gitignore_template):
    for gitignore in github.get_gitignore_templates():
        if gitignore_template.lower() == gitignore.lower():
            return gitignore
    return False

github = authenticate()
user = github.get_user()