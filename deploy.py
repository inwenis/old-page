import os
import subprocess
import stat


def has_hidden_attribute(filepath) -> bool: # type: ignore
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

subprocess.run(["python", "script.py", "build"])
subprocess.run(["git", "checkout", "gh-pages"])
all = os.listdir(".")
all_but_out = [f for f in all if f != "out"]
for f in all_but_out:
    if not has_hidden_attribute(f):
        os.remove(f)

build_result_files = os.listdir("out")
for f in build_result_files:
    os.rename(f"out/{f}", f"./{f}")

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Deploy updated site"])
subprocess.run(["git", "push", "origin", "gh-pages"])
