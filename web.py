import streamlit
import streamlit as sl
import funciones as fn


todos = fn.get_todos()

def add_todo():
    todo = sl.session_state['new_todo'] + "\n"
    todos.append(todo)
    fn.write_todos(todos)




sl.title("Todo App")
sl.subheader("This is my Todo App")
sl.write("Some other text.")






for todo in todos:
    sl.checkbox(todo)


sl.text_input(label="",
              placeholder="Write your todo here",
              on_change=add_todo,
              key="new_todo")

sl.session_state
