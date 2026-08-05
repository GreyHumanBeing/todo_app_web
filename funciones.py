FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a file and returns a list with its content as output.
    """

    with open(filepath, "r") as file_r_local:
        todos_local = file_r_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Receive a list, and write it into a text file in 'w' mode.
    """

    with open(filepath, 'w') as file_w:
        file_w.writelines(todos_arg)


