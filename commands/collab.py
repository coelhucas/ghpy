import click
import utils
from github import Github

@click.command()
@click.argument('action', type=str)
@click.argument('repository', type=str)
@click.argument('user', type=str)
def collab(action, repository, user):
    if action == utils.io.add:
        print('Adding', user, 'as a collaborator on the repository:', repository)
        if utils.auth.check_if_repo_exists(repository):
            repo = utils.user.get_repo(repository)
            add_collaborator(repo, user)

def add_collaborator(repo, user):
    try:
        repo.add_to_collaborators(user)
        print(user, 'was added as a collaborator in', repo.full_name)
    except NameError:
        print(NameError)