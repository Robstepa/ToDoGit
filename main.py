from task import Task
from task_list import TaskList
from os import system


def description_input():
    while True:
        description = input("Describe your task(max 150 symbols): ")
        if len(description) > 150:
            system('clear')
            print("Your description is too long")
            continue
        return description


def name_input():
    while True:
        name = input("Enter your name(max 20 symbols): ")
        if len(name) > 20:
            system('clear')
            print("Your name is too long")
            continue
        return name


def check_index(todo_list):
    while True:
        try:
            task_index = int(input('Enter task index: '))
        except ValueError:
            system('clear')
            print("Index must be a number")
            continue
        task_index -= 1
        if (task_index + 1) > len(todo_list.tasks) or task_index < 0:
            system('clear')
            print('Index does not exist')
            continue
        return task_index


def add_task(todo_list):
    name = name_input()
    description = description_input()
    todo_task = Task(name, description)
    todo_list.add_task(name, description)
    system('clear')
    print('Done\n')


def modify_task(todo_list):
    task_index = check_index(todo_list)
    todo_list.remove_task(task_index)
    name = name_input()
    description = description_input()
    todo_task = Task(name, description)
    todo_list.modify_task(name, description, task_index)
    system('clear')
    print('Done\n')


def delete_task(todo_list):
    task_index = check_index(todo_list)
    todo_list.remove_task(task_index)
    system('clear')
    print('Done\n')


def mark_task(todo_list):
    task_index = check_index(todo_list)
    for item in todo_list.tasks:
        if task_index == todo_list.tasks.index(item):
            item.change_task_status()
    system('clear')
    print('Done\n')


def display_specific_task(todo_list):
    task_index = check_index(todo_list)
    print(todo_list.tasks[task_index])
    print('\n')


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
