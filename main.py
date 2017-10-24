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
        break


def main():
    system('clear')
    todo_list = TaskList()
    menu = '1. Add task\n2. Modify your task\n3. Delete your item\n4. Mark item as done\n5. Display all tasks\n6. Exit'
    while True:
        print('\n')
        print(menu)
        user_input = input("Choose: ")
        system('clear')
        if user_input == '1':
            add_task(todo_list)
        if user_input == '2':
            modify_task(todo_list)
        if user_input == '3':
            delete_task(todo_list)
        if user_input == '4':
            mark_task(todo_list)
        if user_input == '5':
            print(todo_list)
        if user_input == '6':
            break


if __name__ == '__main__':
    main()
