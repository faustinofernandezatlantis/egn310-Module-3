import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        """Initializes a fresh DoublyLinkedList instance before each test."""
        self.dll = DoublyLinkedList()

    def test_append_and_forward_traversal(self):
        """Tests appending items and checking forward string representation."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        self.assertEqual(str(self.dll), "10 -> 20 -> 30 -> None")
        self.assertEqual(len(self.dll), 3)

    def test_prepend(self):
        """Tests prepending items to the front of the list."""
        self.dll.append(20)
        self.dll.prepend(10)
        self.assertEqual(str(self.dll), "10 -> 20 -> None")
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.tail.value, 20)

    def test_reverse_traversal(self):
        """Tests traversing the doubly linked list backwards using reverse_traverse and reverse_str."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        
        # Test reverse generator directly
        reversed_items = list(self.dll.reverse_traverse())
        self.assertEqual(reversed_items, [30, 20, 10])
        
        # Test string formatting for reverse order
        self.assertEqual(self.dll.reverse_str(), "30 <- 20 <- 10 <- None")

    def test_delete_head_and_tail(self):
        """Tests node deletions while ensuring prev/next pointers update correctly."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)

        # Delete head
        self.assertTrue(self.dll.delete(10))
        self.assertEqual(self.dll.head.value, 20)
        self.assertIsNone(self.dll.head.prev)

        # Delete tail
        self.assertTrue(self.dll.delete(30))
        self.assertEqual(self.dll.tail.value, 20)
        self.assertIsNone(self.dll.tail.next)

        self.assertEqual(len(self.dll), 1)

if __name__ == "__main__":
    unittest.main()