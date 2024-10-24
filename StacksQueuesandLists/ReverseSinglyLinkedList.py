"""
3-2. Write a program to reverse the direction of a given singly-linked list. In other
words, after the reversal all pointers should now point backwards. Your algorithm
should take linear time.
"""

from collections import deque

from DataStructures.SinglyLinkedList import SinglyLinkedList, Node

# [Best Approach] Using Iteration (Three Pointers) - O(n) Time and O(1) Space:
# Initialize three pointers: prev as NULL, curr as head, nxt as NULL.
# Iterate through the linked list. In a loop, do the following:
# Store the next node, nxt = curr -> next
# Update the nxt pointer of curr to prev, curr -> nxt = prev
# Update prev as curr and curr as nxt, prev = curr and curr = nxt
def reverse_singly_linked_list_iterative(linked_list: SinglyLinkedList):
    if linked_list.size == 0:
        raise ValueError("List is empty!")
    elif linked_list.size == 1:
        raise ValueError("List has only 1 node!")

    prev = None
    curr = linked_list.head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    temp = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = temp

# [Alternate Approach – 1] Using Stack – O(n) Time and O(n) Space
def reverse_singly_linked_list_stack(linked_list: SinglyLinkedList):
    if linked_list.size == 0:
        raise ValueError("List is empty!")
    elif linked_list.size == 1:
        raise ValueError("List has only 1 node!")

    stack = deque()
    curr = linked_list.head
    while curr != linked_list.tail:
        stack.append(curr)
        curr = curr.next

    curr = linked_list.tail
    while bool(stack):
        curr.next = stack.pop()
        curr = curr.next
    curr.next = None

    temp = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = temp

# [Alternate Approach – 2] Using Recursion – O(n) Time and O(n) Space
def reverse_singly_linked_list_recursive(linked_list: SinglyLinkedList):
    if linked_list.size == 0:
        raise ValueError("List is empty!")
    elif linked_list.size == 1:
        raise ValueError("List has only 1 node!")

    reverse_list_recursive_helper(linked_list.head)

    temp = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = temp

def reverse_list_recursive_helper(head: Node) -> Node:
    if head.next is None:
        return head

    rest = reverse_list_recursive_helper(head.next)
    head.next = None
    rest.next = head

    return rest.next

