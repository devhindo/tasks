import subprocess

def add_to_env(name, val):
    batch = r'add_to_env.bat'
    subprocess.call(["add_to_env.bat", name, val])