from task import Task
from task_list import TaskList
from os import system


def add_task(todo_list):
    while True:
        name = input("Enter your name(max 20 symbols): ")
        if len(name) > 20:
            print("Your name is too long")
            continue
        description = input("Describe your task(max 150 symbols): ")
        if len(description) > 150:
            print("Your description is too long")
            continue
        todo_task = Task(name, description)
        todo_list.add_task(name, description)
        system('clear')
        print('Done\n')
        break


def modify_task(todo_list):
    while True:
        try:
            task_index = int(input('Enter task index: '))
        except ValueError:
            print("Index must be a number")
            continue
        task_index -= 1
        if task_index > len(todo_list.tasks) or task_index < 0:
            print('Index does not exist')
            continue
        todo_list.remove_task(task_index)
        name = input("Enter your name(max 20 symbols): ")
        if len(name) > 20:
            print("Your name is too long")
            continue
        description = input("Describe your task(max 150 symbols): ")
        if len(description) > 150:
            print("Your description is too long")
            continue
        todo_task = Task(name, description)
        todo_list.modify_task(name, description, task_index)
        system('clear')
        print('Done\n')
        break


def delete_task(todo_list):
    while True:
        try:
            task_index = int(input('Enter task index: '))
        except ValueError:
            print("Index must be a number")
            continue
        task_index -= 1
        if task_index > len(todo_list.tasks) or task_index < 0:
            print('Index does not exist')
            continue
        todo_list.remove_task(task_index)
        system('clear')
        print('Done\n')
        break


def mark_task(todo_list):
    while True:
        try:
            task_index = int(input('Enter task index: '))
        except ValueError:
            print("Index must be a number")
            continue
        task_index -= 1
        if task_index > len(todo_list.tasks) or task_index < 0:
            print('Index does not exist')
            continue
        for item in todo_list.tasks:
            if task_index == todo_list.tasks.index(item):
                item.change_task_status()
        system('clear')
        print('Done\n')
        break


def display_specific_task(todo_list):
    while True:
        try:
            task_index = int(input('Enter task index: '))
        except ValueError:
            print("Index must be a number")
            continue
        task_index -= 1
        if task_index > len(todo_list.tasks) or task_index < 0:
            print('Index does not exist')
            continue
        print(todo_list.tasks[task_index])
        print('\n')
        break


def main():
    system('clear')
    todo_list = TaskList()
    print('Welcome to my ToDo program, user...\n')
    menu = '1. Add task\n2. Modify your task\n3. Delete your item\n4. Mark item as done\n' + \
           '5. Display all tasks\n6. Display specific task\n7. Exit'
    while True:
        print(menu)
        user_input = input("Choose: ")
        system('clear')
        if user_input == '1':
            add_task(todo_list)
        if user_input == '7':
            break
        if len(todo_list.tasks) < 1:
            print('There is nothing to show...\n')
            continue
        else:
            if user_input == '2':
                modify_task(todo_list)
            if user_input == '3':
                delete_task(todo_list)
            if user_input == '4':
                mark_task(todo_list)
                system('clear')
            if user_input == '5':
                print(todo_list)
                print('\n')
            if user_input == '6':
                display_specific_task(todo_list)


if __name__ == '__main__':
    main()
