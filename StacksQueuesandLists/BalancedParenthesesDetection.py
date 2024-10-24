"""
3-1. A common problem for compilers and text editors is determining whether the
parentheses in a string are balanced and properly nested. For example, the string
((())())() contains properly nested pairs of parentheses, which the strings )()( and
()) do not. Give an algorithm that returns true if a string contains properly nested
and balanced parentheses, and false if otherwise. For full credit, identify the position
of the first oﬀending parenthesis if the string is not properly nested and balanced.
"""
from collections import deque
from typing import Union

# Steps to detect balanced parentheses:
# 1. Check if the input string contains only '(' and ')' characters, otherwise raise a ValueError.
# 2. Initialize a stack to keep track of the indices of unmatched '('.
# 3. Iterate through the string:
#    - If the character is '(', push its index onto the stack.
#    - If the character is ')', check if there's a matching '(' in the stack:
#      - If so, pop the stack (match found).
#      - If not, return False along with the index of the unbalanced ')'.
# 4. After iteration, check if the stack is empty:
#    - If not, return False with the index of the remaining unmatched '('.
#    - If empty, return True (balanced) with None.
def balanced_parentheses_detection(string: str) -> (bool, Union[int, None]):
    if not all(char in '()' for char in string):
        raise ValueError("Input can only be rounded parentheses: '(' or ')'")

    stack = deque()
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')' and len(stack) > 0:
            stack.pop()
        else:
            return False, i

    if len(stack) != 0:
        i = stack.pop()
        return False, i
    else:
        return True, None



