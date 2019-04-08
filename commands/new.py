import argparse
import utils

__all__ = ['parse_new']


def parse_new():
    parser = argparse.ArgumentParser(description='Controls github from your terminal.')
    repo_creation_group = parser.add_argument_group('creation_group')
    repo_creation_group.add_argument('new', metavar='new', help="Creates a new repository.", type=str, nargs='+', default=False)
    parser.add_argument("name", help="The name of your repo.", type=str)
    parser.add_argument("--license", help="Define the repository initial license", dest='license')
    parser.add_argument("--gitignore", help="Defines your repository .gitignore template", dest='gitignore')

    repo_privacy_group = parser.add_mutually_exclusive_group()
    repo_privacy_group.add_argument("--public", help="Define the repo as public", dest='private', action="store_false")
    repo_privacy_group.add_argument("--private", help="Define the repo as private", dest='private', action="store_true")
    new_repo = parser.parse_args()
    create_repository(new_repo)

def create_repository(new_repo):
    try:
        print("Creating repository", new_repo.name + "...")

        repos = utils.auth.user.get_repos()
        repo_exists = utils.auth.check_if_repo_exists(repos, new_repo.name)
        license = ""
        gitignore = ""

        if new_repo.license and utils.auth.is_license_valid(new_repo.license):
            license = new_repo.license
        elif new_repo.license and utils.auth.is_license_valid(new_repo.license) == False:
            print("The specified license is not valid.")

        if new_repo.gitignore and utils.auth.is_gitignore_valid(new_repo.gitignore):
            gitignore = new_repo.gitignore

        if repo_exists == False:
            utils.user.create_repo(name=new_repo.name, private=new_repo.private, license_template=license, gitignore_template=gitignore)
            print("Successfully created the repository", new_repo.name + ".")
        else:
            print("You already have a repository with this name.")
    except NameError:
        print(NameError)
