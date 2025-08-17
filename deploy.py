import os
import subprocess

subprocess.run(["python", "script.py", "build"])
subprocess.run(["git", "checkout", "gh-pages"])
all = os.listdir(".")
all_but_out = [f for f in all if f != "out"]
for f in all_but_out:
    os.remove(f)

build_result_files = os.listdir("out")
for f in build_result_files:
    os.rename(f"out/{f}", f"./{f}")

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Deploy updated site"])
subprocess.run(["git", "push", "origin", "gh-pages"])
