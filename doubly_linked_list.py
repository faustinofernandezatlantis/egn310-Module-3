class DoublyNode:
    """Represents an individual node in a doubly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly Linked List implementation supporting forward and reverse traversal."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """Adds an element to the end of the list."""
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Adds an element to the beginning of the list."""
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def delete(self, value):
        """Deletes the first occurrence of a value from the list."""
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self._size -= 1
                return True
            current = current.next
        return False

    def reverse_traverse(self):
        """Yields values starting from the tail back to the head."""
        current = self.tail
        while current:
            yield current.value
            current = current.prev

    def reverse_str(self):
        """Returns a string representation of the list in reverse order."""
        return " <- ".join(str(val) for val in self.reverse_traverse()) + " <- None"

    def __len__(self):
        """Returns the current number of items in the list."""
        return self._size

    def __str__(self):
        """Returns a string representation of the list in forward order."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"