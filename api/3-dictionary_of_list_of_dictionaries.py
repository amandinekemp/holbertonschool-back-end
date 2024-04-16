#!/usr/bin/python3
"""Using a REST API, this script retrieves information about all employees'
TODO lists and exports the data to a JSON file."""


import json
import requests


def all_employed_todo():
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f"{base_url}/users"
    todo_url = f"{base_url}/todos"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_data = {}

    # Creating a dictionary of all employees and their tasks
    for user in user_data:
        employee_id = user["id"]
        employee_username = user["username"]
        tasks = [{"username": employee_username, "task": task["title"],
                  "completed": task["completed"]}
                  for task in todo_data if task["userId"] == employee_id]

        employee_data[employee_id] = tasks
    # Exporting the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(employee_data, jsonfile, indent=4)


if __name__ == "__main__":
    all_employed_todo()
