import argparse
import utils
import click

_all_ = ['new']

@click.command()
@click.argument('name', type=str)
@click.option('--private/--public')
@click.option('--license', '-li', type=str)
@click.option('--gitignore', type=str)
def new(name, private, license, gitignore):
    create_repository(name, private, license, gitignore)

def create_repository(name, private, license, gitignore):
    try:
        print("Creating repository", name + "...")

        repos = utils.auth.user.get_repos()
        repo_exists = utils.auth.check_if_repo_exists(repos, name)
        license = ""
        gitignore = ""

        if license and utils.auth.is_license_valid(license):
            license = license
        elif license and utils.auth.is_license_valid(license) == False:
            print("The specified license is not valid.")

        if gitignore and utils.auth.is_gitignore_valid(gitignore):
            gitignore = gitignore

        if repo_exists == False:
            utils.user.create_repo(name=name, private=private, license_template=license, gitignore_template=gitignore)
            print("Successfully created the repository", name + ".")
        else:
            print("You already have a repository with this name.")
    except NameError:
        print(NameError)
