#!/usr/bin/python3
"""
Using urllib.request to interact with a REST API hosted remotely
Write the data to a csv file
"""
import csv
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
    # Loop over the users to get the name of the user whose ID was given
    user_id = int(sys.argv[1])
    for user in users:
        if user.get('id') == user_id:
            name = user.get('name')
            username = user.get('username')
            break
    # Store the todo lists of a given id into a separate list
    user_todos = list()
    user_completed_todos = list()
    completed = 0
    for todo in todos:
        if todo.get('userId') == user_id:
            user_todos.append(todo)
            if todo.get('completed') is True:
                completed = completed + 1
                user_completed_todos.append(todo)
    print("Employee {} is done with tasks({}/{}):".
          format(name, len(user_completed_todos), len(user_todos)))
    for todo in user_completed_todos:
        print("\t {}".format(todo.get('title')))
    # Write the todos that belong to a given user to a csv file
    csv_name = sys.argv[1] + ".csv"
    with open(csv_name, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for user_todo in user_todos:
            csv_row = [user_todo.get('userId'), username,
                       user_todo.get('completed'), user_todo.get('title')]
            csv_writer.writerow(csv_row)


if __name__ == '__main__':
    main()
