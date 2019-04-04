import argparse
import sys
import utils
from github import Github

__all__ = ['parse_rm']

def parse_rm():
    parser = argparse.ArgumentParser(description='Controls github from your terminal.')
    repo_deletion_group = parser.add_argument_group('remove_group')
    repo_deletion_group.add_argument('rm', help="Delete a repository.", type=str, default=False)
    parser.add_argument("name", help="The name of your repo.", type=str)
    args = parser.parse_args()
    remove_repository(args.name)

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
