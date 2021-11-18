## Print list of task descriptions
def print_task_descriptions(list):
    for task in list:
        print(task["description"])


def print_list(list):
    for task in list:
        print_task(task)


def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')



