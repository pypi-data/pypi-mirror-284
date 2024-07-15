from .BaseHandler import BaseHandler
from ..models.Repository import Repository


class CreateGitignoreHandler(BaseHandler):
    def process(self, request: Repository):
        # Prompt for .gitignore content
        ignored_content = input("Please enter files/folders you want to add to .gitignore, separated by comma:\n")
        clean_content_list = [content.strip() for content in ignored_content.split(",")]

        # Create .gitignore file & Write the content to the file
        with open(f"{request.working_directory}/.gitignore", "a") as gitignore:
            for line in clean_content_list:
                gitignore.write(f"\n{line}\n")

        self.move_to_next_handler(request)
