from modules.output import *
from data.task_list import *
from modules.input import *

#use_tasks = input("Do you want to upload some tasks that have already been created ? Y/N ")
#if use_tasks = "Y" : f
 #   from data.task_list import *
  #  ELSE


## Get list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

## Get list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks


## Refactor get_uncompleted_tasks and get_completed_tasks
def get_tasks_by_status(list, status):
    tasks = []
    for task in list:
        if task["completed"] == status:
            tasks.append(tasks)
    return tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_longer_than(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] >= time:
            tasks.append(task)
    return tasks

## Find any task with specific description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
    return "Task Not Found"

# create a task
def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

# add a task to the list
def add_to_list(list, task):
    list.append(task)

def mark_task_complete(task):
    task["completed"] = True

def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("Q or q: Quit")

while (True):
    print_menu()
    option = user_input()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = desc_input()
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        time = int(time_taken())
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        description = desc_input()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = new_task_name()
        time_taken = int(time_taken())
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
