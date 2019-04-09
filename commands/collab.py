import click
import utils
from github import Github

@click.command()
@click.argument('action', type=str)
@click.argument('repository', type=str)
@click.argument('user', type=str)
def collab(action, repository, user):
    if action == utils.io.add:
        if utils.auth.check_if_repo_exists(repository):
            print('Adding', user, 'as a collaborator on the repository:', repository)
            repo = utils.user.get_repo(repository)
            add_collaborator(repo, user)
    elif action == utils.io.rm:
        if utils.auth.check_if_repo_exists(repository):
            print('Removing the collaborator', user, 'of', repository)
            repo = utils.user.get_repo(repository)
            rm_collaborator(repo, user)

def add_collaborator(repo, user):
    try:
        repo.add_to_collaborators(user)
        print(user, 'was added as a collaborator in', repo.full_name)
    except NameError:
        print(NameError)

def rm_collaborator(repo, user):
    try:
        if repo.has_in_collaborators(user):
            repo.remove_from_collaborators(user)
            print(user, "was successfully removed from collaborators of", repo.full_name + ".")
        else:
            print(user, "is not a collaborator of", repo.full_name + ".")
    except NameError:
        print(NameError)