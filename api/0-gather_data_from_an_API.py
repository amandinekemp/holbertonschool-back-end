#!/usr/bin/python3
"""Using a REST API, for a given employee ID, returns information
about his/her"""


import requests
import sys


def employed_todo(employee_id):
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com/"
    # Constructing URLs for user and todo data using the employee ID
    user_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}todos?userId={employee_id}"

    # Sending GET requests to retrieve user and todo data
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    # Extracting JSON data from the responses
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Extracting relevant information from user data
    employee_name = user_data["name"]

    # Counting total number of tasks and completed tasks
    total_number_of_tasks = len(todo_data)
    number_of_done_tasks = sum(1 for task in todo_data if task["completed"])
    # Extracting titles of completed tasks
    completed_tasks_titles = [task["title"]
                              for task in todo_data if task["completed"]]

    # Printing the summary of completed tasks for the employee
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_number_of_tasks
        )
    )
    for task_title in completed_tasks_titles:
        print("\t {}".format(task_title))


if __name__ == "__main__":
    # Retrieving employee ID from command line argument
    employee_id = int(sys.argv[1])
    # Calling the function with the provided employee ID
    employed_todo(employee_id)
