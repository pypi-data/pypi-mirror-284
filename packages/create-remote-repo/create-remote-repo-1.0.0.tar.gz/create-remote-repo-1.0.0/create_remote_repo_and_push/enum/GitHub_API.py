import enum


class GitHubAPI(enum.Enum):
    BASE = "https://api.github.com"
    CREATE_REPO_AUTH_USER = "/user/repos"
