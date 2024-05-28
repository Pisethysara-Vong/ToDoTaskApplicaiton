from ToDoTaskAppFunctions import *
import streamlit as st


def main():
    st.title("To-Do List App with Linked List")
    # Sidebar for adding tasks
    st.sidebar.text_input("Add Task:", key="widget", on_change=submitForAdd)
    task_input = st.session_state.add_task_input
    if st.sidebar.button("Add"):
        if task_input:
            st.session_state.tasks_list.add_task(task_input)

    # Sidebar for removing tasks
    st.sidebar.text_input("Remove Task:", key="widget2", on_change=submitForRemove)
    task_to_remove = st.session_state.remove_task_input
    if st.sidebar.button("Remove"):
        if task_to_remove:
            st.session_state.tasks_list.remove_task(task_to_remove)

    # Main content to display tasks
    st.write("## Your To-Do List:")
    tasks = st.session_state.tasks_list.display_tasks()

    if not tasks:
        st.write("No tasks yet. Add some tasks using the sidebar!")
    else:
        for i, task in enumerate(tasks, start=1):
            st.write(f"{i}. {task}")


if __name__ == "__main__":
    main()
