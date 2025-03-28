import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


todos = functions.get_todos()

st.title("My toDo App")
st.subheader("This is my ToDo App")
st.write("This app is to increase you productivity")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

st.text_input(label="", placeholder="Add new To_Do...",
              on_change=add_todo, key="new_todo")
