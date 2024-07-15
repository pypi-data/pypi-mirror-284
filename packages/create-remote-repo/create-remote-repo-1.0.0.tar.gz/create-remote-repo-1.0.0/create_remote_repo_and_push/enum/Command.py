import enum


class Command(enum.Enum):
    CD = "cd"
    GIT_INIT = "git init"
    GIT_COMMIT = "git commit -m"
    GIT_STAGE_ALL = "git add ."
    GIT_INITIAL_PUSH = "git push --set-upstream origin main"
    ADD_REMOTE_URL_TO_LOCAL_REPO = "git remote add origin"
