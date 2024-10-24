class Node:
    """Class representing a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    """Class representing the singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list
        self.tail = None  # Initialize the tail of the list
        self.size = 0

    def append(self, data):
        """Add a new node with the specified data to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            self.tail = new_node  # Set tail to the new node
            self.size += 1
            return

        self.tail.next = new_node  # Link the new node to the end of the list
        self.tail = new_node  # Update the tail to the new node
        self.size += 1

    def prepend(self, data):
        """Add a new node with the specified data to the beginning of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.tail = new_node  # Update tail to new node
        new_node.next = self.head  # Point new node to current head
        self.head = new_node  # Update head to new node
        self.size += 1

    def delete(self, data):
        """Delete the first node with the specified data."""
        if not self.head:  # If the list is empty
            return

        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next  # Move head to the next node
            if self.head is None:  # If the list is now empty
                self.tail = None  # Set tail to None
            self.size -= 1
            return

        current = self.head
        while current.next:  # Traverse the list
            if current.next.data == data:  # Check for the node to delete
                current.next = current.next.next  # Bypass the node to delete
                # Update the tail if the last node was deleted
                if current.next is None:  # If we deleted the last node
                    self.tail = current
                self.size -= 1
                return

            current = current.next

    def print_list(self):
        """Print the contents of the list."""
        current = self.head
        while current:  # Traverse the list
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list