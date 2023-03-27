import os
home_directory = os.path.expanduser('~')

tasks_folder = home_directory + "\\" + ".tasks"
if not os.path.exists(tasks_folder):
    os.mkdir(tasks_folder)
    print(f"{tasks_folder} folder created successfully...")
    tasks_file = tasks_folder + "\\" + "tasks.txt"
    with open(tasks_file, "w") as f:
        f.write("")
else:
    print(f"{tasks_folder} folder already exists, delete it and try again...")

