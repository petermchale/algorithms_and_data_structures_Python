# https://www.youtube.com/watch?v=IhJGJG-9Dx8&t=10s&list=PLOuZYwbmgZWXvkghUyMLdI90IwxbNCiWK&index=32
# see also: solve-balanced-parentheses-using-PDA.pdf

from stack import Stack


def is_open(char, tokens):
    for pair in tokens:
        left, right = pair
        if char == left:
            return True
    return False


def matches(left_test, right_test, tokens):
    for pair in tokens:
        left, right = pair
        if left_test == left:
            return right_test == right
    return False


def is_balanced(expression):
    print expression
    tokens = [['{', '}'], ['(', ')'], ['[', ']']]
    stack = Stack()
    for char in expression:
        if is_open(char, tokens):
            stack.push(char)
        else:
            if stack.is_empty() or not matches(stack.pop(), char, tokens):
                return False
    return stack.is_empty()

if __name__ == '__main__':

    print 'is balanced?', is_balanced('{()[{({})[]()}]}([])')
