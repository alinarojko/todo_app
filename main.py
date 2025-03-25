from functions import get_todos, write_todo
# or: import functions
# and when you ask the function you should write
# todos = functions.get_todos()
import time
now = time.strftime("%H:%M:%S , %d %b, %Y")
print("It is ", now)

while True:
    user_action = input('Type add, show, edit, exit or complete: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # everything after element number 4 , will be recorded to the list (can be any number) so if user enter
        # add new task , 'add ' will be not recorded

        todos = get_todos()
        todos.append(todo + '\n')    # to add new item to the existing list

        write_todo(todos)


    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.title()   # to make title fot each item
            item = item.strip('\n') # to remove part of the string
            result = f'{index + 1}.{item}'
            print(result)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo : ')
            todos[number] = new_todo + '\n'

            write_todo(todos)

        except ValueError:
            print('Your command is not valid.')
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number -1
            print(f'Your : ', (todos[index]).strip('\n'),'will be removed from the list')
            todos.pop(index)

            write_todo(todos)
            print(f'Greate , this task , {(todos[index]).strip('\n')}, is completed')

        except IndexError:
            print('No item with such number')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Use correct command ')

print('Buy!')
