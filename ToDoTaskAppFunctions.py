import streamlit as st


# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_task(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.data == task:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next

    def display_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append(current.data)
            current = current.next

        return tasks


# Initialize a linked list in session state if not already present
if 'tasks_list' not in st.session_state:
    st.session_state.tasks_list = LinkedList()
# Initialize the session state for input values if not already present
if 'add_task_input' not in st.session_state:
    st.session_state.add_task_input = ""
if 'remove_task_input' not in st.session_state:
    st.session_state.remove_task_input = ""


def submitForAdd():
    st.session_state.add_task_input = st.session_state.widget
    st.session_state.widget = ""


def submitForRemove():
    st.session_state.remove_task_input = st.session_state.widget2
    st.session_state.widget2 = ""

