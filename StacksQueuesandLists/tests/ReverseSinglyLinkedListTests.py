import unittest
from abc import ABC, abstractmethod
from DataStructures.SinglyLinkedList import SinglyLinkedList
from ..ReverseSinglyLinkedList import reverse_singly_linked_list_stack, reverse_singly_linked_list_recursive, \
    reverse_singly_linked_list_iterative


class _BaseTestReverseSinglyLinkedList(unittest.TestCase, ABC):
    """Base class to define test logic and helpers for reversing linked lists."""

    @abstractmethod
    def reverse_function(self, linked_list):
        """Abstract method that must be implemented by subclasses."""
        pass

    def setUp(self):
        """Set up an empty linked list for testing."""
        self.linked_list = SinglyLinkedList()

    def add_elements(self, elements):
        """Helper function to add multiple elements to the linked list."""
        for element in elements:
            self.linked_list.append(element)

    def check_reversed_list(self, expected):
        """Helper function to check if the list was reversed correctly."""
        current = self.linked_list.head
        for value in expected:
            self.assertEqual(current.data, value)
            current = current.next
        self.assertIsNone(current)

    def test_reverse_empty_list(self):
        """Test reversing an empty list should raise ValueError."""
        with self.assertRaises(ValueError):
            self.reverse_function(self.linked_list)

    def test_reverse_single_node_list(self):
        """Test reversing a single node list should raise ValueError."""
        self.add_elements([1])
        with self.assertRaises(ValueError):
            self.reverse_function(self.linked_list)

    def test_reverse_two_node_list(self):
        """Test reversing a two-node list."""
        self.add_elements([1, 2])
        self.reverse_function(self.linked_list)
        self.check_reversed_list([2, 1])

    def test_reverse_multiple_node_list(self):
        """Test reversing a list with multiple nodes."""
        self.add_elements([1, 2, 3, 4])
        self.reverse_function(self.linked_list)
        self.check_reversed_list([4, 3, 2, 1])

class TestReverseSinglyLinkedListIterative(_BaseTestReverseSinglyLinkedList):
    """Test class for recursive reversal of singly linked list."""

    def reverse_function(self, linked_list):
        """Implement the recursive reversal function."""
        reverse_singly_linked_list_iterative(linked_list)


class TestReverseSinglyLinkedListStack(_BaseTestReverseSinglyLinkedList):
    """Test class for stack-based reversal of singly linked list."""

    def reverse_function(self, linked_list):
        """Implement the stack-based reversal function."""
        reverse_singly_linked_list_stack(linked_list)


class TestReverseSinglyLinkedListRecursive(_BaseTestReverseSinglyLinkedList):
    """Test class for recursive reversal of singly linked list."""

    def reverse_function(self, linked_list):
        """Implement the recursive reversal function."""
        reverse_singly_linked_list_recursive(linked_list)

if __name__ == '__main__':
    unittest.main()