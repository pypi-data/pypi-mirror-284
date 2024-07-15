from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='create-remote-repo',
    version="1.0.0",
    author='Kim Chung',
    author_email='kchung0802@gmail.com',
    license='MIT License',
    description='This tool automate the process of creating a repo from your current working directory and pushing '
                'it to your remote Github.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        create-remote-repo=create_remote_repo_and_push.create_remote_repo_and_push:main
    '''
)
