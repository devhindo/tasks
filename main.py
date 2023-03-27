import os
import operations
import queue

home_directory = os.path.expanduser('~')
tasks_folder = home_directory + "\\" + ".tasks"
tasks_file = tasks_folder + "\\" + "tasks.txt"

if not os.path.exists(tasks_folder):
    os.mkdir(tasks_folder)
    print(f"{tasks_folder} folder created successfully...")
    with open(tasks_file, "w") as f:
        f.write("")
else:
    print(f"{tasks_folder} folder already exists, delete it and try again...")

tasks = queue.Queue()
operations.load_tasks(tasks, tasks_file)

