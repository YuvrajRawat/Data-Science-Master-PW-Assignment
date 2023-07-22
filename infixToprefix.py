import sys

expr = sys.argv[1]

def InfixToPrefix(expr):
    # Function to get the precedence of an operator
    def getPrecedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0  # For opening and closing parentheses

    # Function to reverse a string
    def reverseString(s):
        return s[::-1]

    # Function to check if a character is an operand (letter or digit)
    def isOperand(char):
        return char.isalpha() or char.isdigit()

    # Reversing the infix expression
    expr = reverseString(expr)

    # Stack to store operators and parentheses
    stack = []
    # Result string to store the prefix expression
    result = ""

    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # Discard the opening parenthesis
        elif isOperand(char):
            result += char
        else:  # Operator
            while stack and (getPrecedence(stack[-1]) > getPrecedence(char) or (getPrecedence(stack[-1]) == getPrecedence(char) and stack[-1] != '(')):
                result += stack.pop()
            stack.append(char)

    # Pop any remaining operators from the stack
    while stack:
        result += stack.pop()

    # Reverse the result string to obtain the prefix expression
    result = reverseString(result)

    return result

print(InfixToPrefix(expr))
