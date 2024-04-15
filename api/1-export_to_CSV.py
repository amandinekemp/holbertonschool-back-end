#!/usr/bin/python3
"""Using a REST API, for a given employee ID, returns information about his/her"""


import csv
import requests
import sys


def employed_todo(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    employee_username = user_data["username"]

    total_number_of_tasks = len(todo_data)
    number_of_done_tasks = sum(1 for task in todo_data if task["completed"])
    completed_tasks_titles = [task["title"] for task in todo_data if task["completed"]]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_number_of_tasks
        )
    )
    for task_title in completed_tasks_titles:
        print("\t {}".format(task_title))

    with open(f"{employee_id}.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            csvwriter.writerow(
                [employee_id, employee_username, str(task["completed"]), task["title"]]
            )


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    employed_todo(employee_id)
