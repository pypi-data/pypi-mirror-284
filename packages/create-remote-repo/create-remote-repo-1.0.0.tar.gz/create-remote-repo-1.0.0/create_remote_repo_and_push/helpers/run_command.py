import subprocess


def run_command(command):
    # shell=True: This argument specifies that the command should be executed through the shell.
    # This allows you to run complex shell commands and use shell features like wildcard expansion.

    # check=True: If set to True, this argument makes the subprocess.run function raise a subprocess.CalledProcessError
    # exception if the command returns a non-zero exit code, indicating an error.

    # stdout=subprocess.PIPE: This argument redirects the standard output (stdout) of the command to a pipe,
    # allowing the output to be captured and processed in the Python script.

    # stderr=subprocess.PIPE: Similar to stdout. But it redirects standard error to a pipe instead.
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode().strip()  # Decode the byte string returned by result.stdout to a regular string.
