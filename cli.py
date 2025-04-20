# from functions import get_todos, write_todos
import functions
from builtins import *
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input(f"What do you want to edit '{todos[number].strip("\n")}' to: ")
            todos[number] = new_todo + "\n"
            print(f"Todo # {number + 1} has been successfully edited!")

            functions.write_todos(todos)

        except ValueError:
            print("Type only number. Please try again.")

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            print(f"Todo '{todos[number - 1].strip("\n")}' has been successfully completed!")
            todos.pop(number - 1)

            functions.write_todos(todos)

        except IndexError:
            print("Index is out of range. Please try again")
    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid Input. Please Try Again.")

print("")
print("Thank you for using our app! BYE!")