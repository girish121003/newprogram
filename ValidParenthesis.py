'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.'''
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    matching_dict = {"(": ")", "{": "}", "[": "]"}
    # Add one empty str in the stack so we won't pop from empty list
    matching_stack = [""]
    for i in s:
        if i in matching_dict:
            matching_stack.append(matching_dict[i])
        elif i in matching_dict.values() and i != matching_stack.pop():
            return False
    return matching_stack == [""]

k=input("Enter the valid String in terms of parenthesis : ")
result=isValid(k)
print(result)