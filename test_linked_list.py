import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Runs before each test method to initialize a fresh LinkedList instance."""
        self.ll = LinkedList()

    def test_append_and_str(self):
        """Tests appending items and checking string formatting."""
        self.ll.append(10)
        self.ll.append(20)
        self.assertEqual(str(self.ll), "10 -> 20 -> None")
        self.assertEqual(len(self.ll), 2)

    def test_prepend(self):
        """Tests prepending items to the front of the list."""
        self.ll.append(10)
        self.ll.prepend(5)
        self.assertEqual(str(self.ll), "5 -> 10 -> None")
        self.assertEqual(len(self.ll), 2)

    def test_find(self):
        """Tests finding existing and non-existing values."""
        self.ll.append(10)
        self.ll.append(20)
        self.assertTrue(self.ll.find(10))
        self.assertFalse(self.ll.find(99))

    def test_delete_head(self):
        """Tests deleting the head node."""
        self.ll.append(10)
        self.ll.append(20)
        result = self.ll.delete(10)
        self.assertTrue(result)
        self.assertEqual(str(self.ll), "20 -> None")
        self.assertEqual(len(self.ll), 1)

    def test_delete_middle(self):
        """Tests deleting a middle node."""
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)
        self.ll.delete(20)
        self.assertEqual(str(self.ll), "10 -> 30 -> None")

    def test_delete_not_found(self):
        """Tests trying to delete a value that does not exist."""
        self.ll.append(10)
        result = self.ll.delete(99)
        self.assertFalse(result)
        self.assertEqual(len(self.ll), 1)

if __name__ == "__main__":
    unittest.main()