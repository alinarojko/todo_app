FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    ''' Read a text file and return the of
     todo items. Default argument direct to the file
     where the todo list is stored . '''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todo(todos_arg, filepath=FILEPATH):
    ''' Write new todo to the existing file '''
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


