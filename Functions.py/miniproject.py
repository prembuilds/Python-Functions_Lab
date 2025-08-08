'''Simple To-Do Manager Using Functional Programming
Objective: Manage a list of to-do tasks using functions, lambda, filter, and map.
Requirements:
● Allow adding tasks using a function add_task(task_list, task_name).
● Each task is a dictionary: { "name": str, "completed": bool }.
● Use lambda and filter() to list only incomplete tasks.
● Use map() to mark all tasks as completed.
● Include a search_tasks(task_list, keyword) function using filter() and lambda.
Sample Workflow:
tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")
# List incomplete tasks
print("Pending Tasks:", list_pending(tasks))'''



tasks = []

def add_task(task_list, task_name):
    task = {"name": task_name, "completed": False}
    return task_list + [task]

def list_pending(task_list):
    return list(filter(lambda task: not task["completed"], task_list))

def complete_all_tasks(task_list):
    return list(map(lambda task: {**task, "completed": True}, task_list))

def search_tasks(task_list, keyword):
    return list(filter(lambda task: keyword.lower() in task["name"].lower(), task_list))

tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

print("All Tasks:")
for task in tasks:
    print(f"- {task['name']} (Completed: {task['completed']})")

print("\nPending Tasks:")
for task in list_pending(tasks):
    print(f"- {task['name']}")

tasks = complete_all_tasks(tasks)

print("\nTasks After Completing All:")
for task in tasks:
    print(f"- {task['name']} (Completed: {task['completed']})")

print("\nSearch for 'call':")
for task in search_tasks(tasks, "call"):
    print(f"- {task['name']}")
