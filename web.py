import streamlit as sl
import funciones as fn


todos = fn.get_todos()

def add_todo():
    if sl.session_state['new_todo'] != "":
        todo_local = sl.session_state["new_todo"] + '\n'
        if todo_local not in todos:  # Add this if-condition to fix the issue
            todos.append(todo_local)
            fn.write_todos(todos)
            sl.session_state['new_todo'] = ""

sl.title("Todo App")
sl.subheader("This is my Todo App")
sl.write("Some other text.")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del sl.session_state[todo]
        sl.rerun()

sl.text_input(label="",
              placeholder="Write your todo here",
              on_change=add_todo,
              key="new_todo")
