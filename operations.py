def load_tasks(tasks, file):
    with open(file, 'r') as file:
        for line in file:
            tasks.put(line.strip())



