import unittest

from StacksQueuesandLists.DynamicArrayWithShrink import DynamicArrayWithShrink


class TestDynamicArrayWithShrink(unittest.TestCase):

    def setUp(self):
        """Set up a new DynamicArrayWithShrink instance for testing."""
        self.dynamic_array = DynamicArrayWithShrink(capacity=2)

    def test_initial_size(self):
        """Test that the initial size is zero."""
        self.assertEqual(self.dynamic_array.get_size(), 0)

    def test_add_elements(self):
        """Test adding elements and ensure size updates correctly."""
        self.dynamic_array.add(1)
        self.dynamic_array.add(2)
        self.assertEqual(self.dynamic_array.get_size(), 2)

        # Test that adding a third element causes a growth
        self.dynamic_array.add(3)
        self.assertEqual(self.dynamic_array.get_size(), 3)

    def test_pop_element(self):
        """Test popping elements and ensure size decreases correctly."""
        self.dynamic_array.add(1)
        self.dynamic_array.add(2)
        self.dynamic_array.add(3)

        popped = self.dynamic_array.pop()
        self.assertEqual(popped, 3)
        self.assertEqual(self.dynamic_array.get_size(), 2)

    def test_shrink_on_pop(self):
        """Test that the array shrinks when popping elements."""
        for i in range(1, 6):
            self.dynamic_array.add(i)  # Fill the array

        for _ in range(4):  # Pop elements
            self.dynamic_array.pop()

        # After 4 pops, the array should shrink
        self.assertEqual(self.dynamic_array.capacity, 2)  # Capacity should be halved

    def test_remove_first(self):
        """Test removing the first element."""
        self.dynamic_array.add(1)
        self.dynamic_array.add(2)
        self.dynamic_array.add(3)

        removed = self.dynamic_array.remove_first()
        self.assertEqual(removed, 1)
        self.assertEqual(self.dynamic_array.get_size(), 2)

    def test_shrink_on_remove_first(self):
        """Test that the array shrinks when removing the first element."""
        for i in range(1, 6):
            self.dynamic_array.add(i)  # Fill the array

        for _ in range(4):  # Remove elements
            self.dynamic_array.remove_first()

        # After 4 removals, the array should shrink
        self.assertEqual(self.dynamic_array.capacity, 2)  # Capacity should be halved

    def test_remove_index(self):
        """Test removing an element at a specific index."""
        self.dynamic_array.add(1)
        self.dynamic_array.add(2)
        self.dynamic_array.add(3)

        removed = self.dynamic_array.remove_index(1)  # Remove the element at index 1
        self.assertEqual(removed, 2)
        self.assertEqual(self.dynamic_array.get_size(), 2)

    def test_shrink_on_remove_index(self):
        """Test that the array shrinks when removing an element by index."""
        for i in range(1, 8):
            self.dynamic_array.add(i)  # Fill the array

        for i in range(5):
            # Remove first element
            self.dynamic_array.remove_index(0)

        # After 2 removals, the array should shrink
        self.assertEqual(self.dynamic_array.capacity, 4)  # Capacity should be halved

    def test_find_existing_object(self):
        """Test finding an existing object."""
        self.dynamic_array.add(1)
        self.dynamic_array.add(2)
        index = self.dynamic_array.find(1)
        self.assertEqual(index, 0)

    def test_find_non_existing_object(self):
        """Test finding a non-existing object raises an error."""
        self.dynamic_array.add(1)
        self.dynamic_array.add(2)
        with self.assertRaises(ValueError):
            self.dynamic_array.find(3)

if __name__ == '__main__':
    unittest.main()