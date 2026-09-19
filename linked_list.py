class Node:
    """Represents an individual node in the singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly Linked List implementation."""
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """Adds an element to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Adds an element to the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def delete(self, value):
        """Deletes the first occurrence of a value from the list."""
        if not self.head:
            return False

        # If the target value is at the head
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        # Search for the value in the rest of the list
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

    def find(self, value):
        """Returns True if the value exists in the list, False otherwise."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        """Returns the current number of items in the list."""
        return self._size

    def __str__(self):
        """Returns a string representation of the list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"