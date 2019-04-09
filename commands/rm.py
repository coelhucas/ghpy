import sys
import utils
import click
from github import Github

@click.command()
@click.argument('name', type=str)
def rm(name):
    remove_repository(name)

def remove_repository(repo_name):
    try:
        repo = utils.user.get_repo(repo_name)
        if repo:
            print("Are you sure? This is going to delete your entire \"" + repo_name + "\"'s repo. (Y)es/(N)o:")
            response = sys.stdin.read(1)
            if (response.lower() == "y"):
                repo.delete()
                print("Successfully deleted the repository named", repo_name + ".")
    except:
        print("Error: The specified repository probably doesn't exist.")
