import os
import subprocess
import stat


def has_hidden_attribute(filepath) -> bool: # type: ignore
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

subprocess.run(["python", "scripts/run.py", "build"])
subprocess.run(["git", "checkout", "gh-pages"])
to_remove = os.listdir(".")
to_remove = [f for f in to_remove if f != "out"] # do not remove out because the files to be deplyed are there
to_remove = [f for f in to_remove if f != ".vscode"] # do not remove .vscode as it's locked by vs code
for f in to_remove:
    if not has_hidden_attribute(f):
        os.remove(f)

build_result_files = os.listdir("out")
for f in build_result_files:
    os.rename(f"out/{f}", f"./{f}")

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Deploy updated site", "--allow-empty"])
subprocess.run(["git", "push", "origin", "gh-pages"])
subprocess.run(["git", "checkout", "-"]) # back to previous branch
