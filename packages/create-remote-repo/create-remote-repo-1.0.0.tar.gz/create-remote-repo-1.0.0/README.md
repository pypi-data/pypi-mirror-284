# GitHub Repo Automation Tool

This command line tool automates the process of initializing a local Git repository, creating a remote GitHub repository via the GitHub API, optionally adding a `.gitignore` file, staging changes, committing, and performing the initial push to the remote repository.

## Features

- Initialize a local Git repository.
- Create a remote repository on GitHub.
- Optionally add a `.gitignore` file.
- Stage changes.
- Commit changes.
- Push the initial commit to the remote repository.

## Requirements

- Python 3.x
- Git
- GitHub account and authorization token

## Installation

## Usage
```bash
python create-remote-repo -rn <repo-name> -gu <github-username> -t <github-token> -d <working-directory> [-i <include-gitignore>] [-p <private>]
```

## Example
```bash
python create-remote-repo -rn my-new-repo -gu myusername -t mytoken -d /path/to/working/directory -i y -p y
```

This command will:

1. Initialize a Git repository in the specified local working directory.
2. Create a remote repository named my-new-repo under the GitHub account myusername.
3. Add a .gitignore file to the repository.
4. Stage all changes.
5. Commit the changes.
6. Push the initial commit to the private remote repository.

## CLI Arguments
| Argument                     | Description                                                                                      | Required | Default Value            |
|------------------------------|--------------------------------------------------------------------------------------------------|----------|--------------------------|
| `-rn`, `--repo-name`         | The name of the remote repository you want to create.                                            | Yes      | None                     |
| `-gu`, `--github-username`   | The username of your GitHub account.                                                             | No       | `global_github_username` |
| `-t`, `--github-token`       | Your GitHub authorization token.                                                                 | No       | `global_github_token`    |
| `-d`, `--working-directory`  | The absolute path to the local working directory where the repository should be initialized.     | Yes      | None                     |
| `-i`, `--include-gitignore`  | Enter `y` if you want to add a `.gitignore` file to your repository, otherwise enter `n`.        | No       | `n`                      |
| `-p`, `--private`            | Enter `y` if you want to make the remote repository private, otherwise enter `n`.                | No       | `n`                      |

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Kimmm-c/automate-create-remote-repo/blob/9c1d5213b39def985fc7cbfb1c4f15a2e7b74b57/LICENSE) file for details.

## Acknowledgements
Created and maintained by Kim Chung.
