#!/usr/bin/python3
"""Retrieves information about the progress of an employee's task list
matching the specified id."""
import requests
from sys import argv

api_url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    # Retrieves employee information from the API
    data = requests.get(f"{api_url}/users/{argv[1]}")
    employee_data = data.json()

    # Retrieves the employee's tasks from the API
    list_tasks = requests.get(f"{api_url}/todos?userId={argv[1]}")
    tasks_data = list_tasks.json()

    # Filters completed tasks
    tasks_complete = [task for task in tasks_data if task["completed"]]

    # Retrieves the employee's name
    employee_name = employee_data["name"]
    # Number of completed tasks
    nb_tasks_done = len(tasks_complete)
    # Total number of tasks
    total_task = len(tasks_data)

    # Displays information about the progress of the task list
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, nb_tasks_done, total_task
        )
    )

    # Displays the list of completed tasks
    for task in tasks_complete:
        print(f"\t {task['title']}")
