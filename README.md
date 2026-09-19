# egn310-Module-3
# Data Structures: Linked List Implementation

A comprehensive Python implementation of Singly Linked List and Doubly Linked List data structures, fully covered with automated unit tests.

##  Features

### Singly Linked List (`LinkedList`)
- **`append(value)`**: Adds a new element to the tail of the list.
- **`prepend(value)`**: Adds a new element to the head of the list.
- **`delete(value)`**: Removes the first occurrence of a target value.
- **`find(value)`**: Searches for an element and returns a boolean status.
- Support for `len()` and formatted string outputs (`str()`).

### Doubly Linked List (`DoublyLinkedList`) — Extension Track
- Maintains references to both `head` and `tail` nodes.
- Bidirectional node pointers (`next` and `prev`).
- **`reverse_traverse()`**: Generator function to iterate through the list backwards.
- **`reverse_str()`**: Returns a string representation in reverse order.

---

##  Repository Structure

```text
.
├── linked_list.py           # SinglyLinkedList and Node classes
├── doubly_linked_list.py    # DoublyLinkedList and DoublyNode classes
├── test_linked_list.py      # Unit tests for SinglyLinkedList
├── test_doubly_linked_list.py # Unit tests for DoublyLinkedList
└── README.md                # Project documentation
```
Getting Started

Prerequisites
Python 3.8+ (No external third-party packages required).

Running Unit Tests
You can run each test file individually using Python's built-in unittest module:

Bash
# Run Singly Linked List tests
python3 -m unittest test_linked_list.py

# Run Doubly Linked List tests
python3 -m unittest test_doubly_linked_list.py
Or run all unit tests in the repository at once:

Bash
python3 -m unittest discover

<ElicitationsGroup message="Is your GitHub repository ready to be submitted, or should we work on the next assignment?">
  <Elicitation label="Move on to the next assignment" query="Let's move on to the next assignment."/>
  <Elicitation label="Help with Git commands to push this code" query="Can you give me the Git commands to create a repository and push this project to GitHub?"/>
</ElicitationsGroup>
