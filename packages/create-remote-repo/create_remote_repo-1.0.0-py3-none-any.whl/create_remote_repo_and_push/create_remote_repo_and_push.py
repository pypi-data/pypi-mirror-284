from .models.Repository import Repository
from .handlers.CreateRemoteRepoHandler import CreateRemoteRepoHandler
from .handlers.CreateGitignoreHandler import CreateGitignoreHandler
import argparse
import os

username = os.getenv('GITHUB_USERNAME')
token = os.getenv('GITHUB_TOKEN')


def validate_request(request):
    if request.repo_name is None:
        raise ValueError("Remote repository name is required")
    elif request.working_directory is None or not os.path.exists(request.working_directory):
        raise ValueError("Path to working directory is either not provided or invalid")
    elif request.github_token is None or request.github_username is None:
        raise ValueError("No GitHub token or username found. Please check your global variables or manually enter them")


def setup_request_commandline() -> Repository:
    parser = argparse.ArgumentParser()
    parser.add_argument("-rn", "--repo-name",
                        help="The name of the remote repository you want to create")
    parser.add_argument("-gu", "--github-username",
                        help="The username of your Github account",
                        default=username)
    parser.add_argument("-t", "--github-token",
                        help="Your Github authorization token",
                        default=token)
    parser.add_argument("-d", "--working-directory",
                        help="The absolute path to local working directory, where the repo should be initialized")
    parser.add_argument("-i", "--include-gitignore",
                        help="Enter y if you want to add .gitignore to your repo, otherwise enter n",
                        default="n")
    parser.add_argument("-p", "--private",
                        help="Enter y if you want to make the remote repo private, otherwise enter n",
                        default="n")

    try:
        args = parser.parse_args()
        repo = Repository(repo_name=args.repo_name,
                          github_username=args.github_username,
                          github_token=args.github_token,
                          working_directory=args.working_directory,
                          include_gitignore=args.include_gitignore,
                          is_private=args.private)
        validate_request(repo)
        return repo

    except Exception as e:
        print(f'Error: {e}')
        quit()


def main():
    repo = setup_request_commandline()

    create_repo_handler = CreateRemoteRepoHandler()

    if repo.include_gitignore:
        create_gitignore_handler = CreateGitignoreHandler()
        create_gitignore_handler.set_next_handler(create_repo_handler)
        try:
            create_gitignore_handler.process(repo)
        except Exception as e:
            print(e)
    else:
        try:
            create_repo_handler.process(repo)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
