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

# def balanced_parentheses_detection_Alt(string: str) -> (bool, Union[int, None]):
#     if not all(char in '()' for char in string):
#         raise ValueError("Input can only be rounded parentheses: '(' or ')'")
#
#     count = 0
#     for i, char in enumerate(string):
#         if char == '(':
#             count += 1
#         else:
#             count -= 1
#
#         if count < 0:
#             return False, i
#
#     if count == 0:
#         return True, None



