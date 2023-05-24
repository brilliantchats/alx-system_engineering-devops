#!/usr/bin/python3
"""
Using urllib.request to interact with a REST API hosted remotely
"""
import json
import sys
from urllib.request import urlopen


def main():
    # Gets all the todos from {JSON} Placeholder remote site
    with urlopen('https://jsonplaceholder.typicode.com/todos') as t_resp:
        todo_json = t_resp.read()

    # Load the todos into a list using json
    todos = json.loads(todo_json)
    # Gets all the users from {JSON} Placeholder remote site
    with urlopen('https://jsonplaceholder.typicode.com/users') as u_resp:
        users_json = u_resp.read()

    # Load the users into a list of dictionaries using json
    users = json.loads(users_json)
    # Dictionary to contain every user id as key, with value being todos
    users_todos = dict()
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_task_list = list()
        for todo in todos:
            if user_id == todo.get('userId'):
                task_dict = dict()
                task_dict['username'] = username
                task_dict['task'] = todo.get('title')
                task_dict['completed'] = todo.get('completed')
                user_task_list.append(task_dict)
        users_todos[user_id] = user_task_list
    # Load the users todo list into a json file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_writer:
        json.dump(users_todos, json_writer)


if __name__ == '__main__':
    main()
