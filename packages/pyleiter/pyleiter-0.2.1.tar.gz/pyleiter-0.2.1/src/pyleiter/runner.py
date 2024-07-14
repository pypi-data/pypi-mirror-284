import sys
import subprocess


def run_process(command):
    print(f"Running process {command}...")
    with subprocess.Popen(command.split(" "), stdout=subprocess.PIPE) as process:
        for line in iter(process.stdout.readline, b""):
            sys.stdout.write(line.decode("utf-8"))

    print(f"Process {command} finished!")
