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
