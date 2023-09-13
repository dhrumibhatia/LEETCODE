# 20. Valid Parentheses
#approach 1
def is_valid(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top_element = stack.pop()
            if char == ')' and top_element != '(':
                return False
            if char == '}' and top_element != '{':
                return False
            if char == ']' and top_element != '[':
                return False
    return not stack

#approach 2
# brackets = {'{': '}', '(': ')', '[': ']'}
# stack = []
# for char in s:
#    if char in brackets:
#         stack.append(char)
#    elif not stack or brackets[stack.pop()] != char:
#         return False
            
# return not stack

# s = "()"
# s = "()[]{}"
s = "(){]{}"
print(is_valid(s))
print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True