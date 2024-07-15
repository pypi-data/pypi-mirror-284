from .BaseHandler import BaseHandler
from ..enum.Command import Command
from ..helpers.run_command import run_command as rc
from ..models.Repository import Repository
from ..enum.GitHub_API import GitHubAPI as apis
import requests


class CreateRemoteRepoHandler(BaseHandler):
    def process(self, request: Repository):
        # Create local repo, stage the changes, and commit.
        rc(f"{Command.CD.value} {request.working_directory} "
           f"&& {Command.GIT_INIT.value} "
           f"&& {Command.GIT_STAGE_ALL.value} "
           f"&& {Command.GIT_COMMIT.value} \'Initial commit\'")

        # Create a new repo on GitHub
        res = requests.post(
            f"{apis.BASE.value}{apis.CREATE_REPO_AUTH_USER.value}",
            json={'name': request.repo_name, 'private': request.is_private},
            auth=(request.github_username, request.github_token)
        )
        if res.status_code != 201:
            print(f'remote repo creation failed. {res.json()}')
            raise Exception("Github Api call fails")
        remote_clone_url = res.json()['clone_url']

        # Add the remote clone url to the local git repo and push the local changes to the remote origin
        rc(f"{Command.CD.value} {request.working_directory} "
           f"&& {Command.ADD_REMOTE_URL_TO_LOCAL_REPO.value} {remote_clone_url} "
           f"&& {Command.GIT_INITIAL_PUSH.value}")

        self.move_to_next_handler(request)
