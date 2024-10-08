import unittest
from StacksQueuesandLists.BalancedParenthesesDetection import balanced_parentheses_detection

class TestBalancedParentheses(unittest.TestCase):

    # Test cases for the balanced_parentheses_detection function
    def test_balanced_parentheses_detection(self):
        self.assertEqual(balanced_parentheses_detection("((())())()"), (True, None))
        self.assertEqual(balanced_parentheses_detection("()()()"), (True, None))
        self.assertEqual(balanced_parentheses_detection("(()())"), (True, None))
        self.assertEqual(balanced_parentheses_detection(")("), (False, 0))
        self.assertEqual(balanced_parentheses_detection("(()"), (False, 0))
        self.assertEqual(balanced_parentheses_detection("())"), (False, 2))
        self.assertEqual(balanced_parentheses_detection(")("), (False, 0))
        self.assertEqual(balanced_parentheses_detection("((()"), (False, 1))
        self.assertEqual(balanced_parentheses_detection("()()())"), (False, 6))
        self.assertEqual(balanced_parentheses_detection(""), (True, None))  # Empty string case
        self.assertEqual(balanced_parentheses_detection("(((((())))))"), (True, None))  # Deep nesting

        with self.assertRaises(ValueError) as context:
            balanced_parentheses_detection("a(b)c")  # Should raise ValueError
        self.assertEqual(str(context.exception), "Input can only be rounded parentheses: '(' or ')'")

    # Test cases for the balanced_parentheses_detection_Alt function
    # def test_balanced_parentheses_detection_Alt(self):
    #     self.assertEqual(balanced_parentheses_detection_Alt("((())())()"), (True, None))
    #     self.assertEqual(balanced_parentheses_detection_Alt("()()()"), (True, None))
    #     self.assertEqual(balanced_parentheses_detection_Alt("(()())"), (True, None))
    #     self.assertEqual(balanced_parentheses_detection_Alt(")("), (False, 0))
    #     self.assertEqual(balanced_parentheses_detection_Alt("(()"), (False, 0))
    #     self.assertEqual(balanced_parentheses_detection_Alt("())"), (False, 2))
    #     self.assertEqual(balanced_parentheses_detection_Alt(")("), (False, 0))
    #     self.assertEqual(balanced_parentheses_detection_Alt("((()"), (False, 1))
    #     self.assertEqual(balanced_parentheses_detection_Alt("()()())"), (False, 6))
    #     self.assertEqual(balanced_parentheses_detection_Alt(""), (True, None))  # Empty string case
    #     self.assertEqual(balanced_parentheses_detection_Alt("(((((())))))"), (True, None))  # Deep nesting
    #
    #     with self.assertRaises(ValueError) as context:
    #         balanced_parentheses_detection_Alt("a(b)c")  # Should raise ValueError
    #     self.assertEqual(str(context.exception), "Input can only be rounded parentheses: '(' or ')'")

if __name__ == '__main__':
    unittest.main()