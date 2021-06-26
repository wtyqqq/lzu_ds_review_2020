class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("Perform pop stack operation from empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


def is_balanced(string1):
    if (string1.count("(") == string1.count(")")) and (string1.count("{") == string1.count("}")) and (
            string1.count("<") == string1.count(">") and (string1.count("[") == string1.count("]"))):
        return True
    else:
        return False


def is_balanced_2(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()


def shorten(str1, length):
    return str1[:length - 3] + "..."


def simplify(str1):
    r""" Returns the text with multiple spaces reduced to single spaces
    The whitespace parameter is a string of characters,
    each of which is considered to be a space.
    If delete is not empty it should be a string, in which case any
    characters in the delete string are excluded from the resultant
    string.
    >>> simplify(" this and\n that\t too")
    'this and that too'
    >>> simplify(" Washington D.C.\n")
    'Washington D.C.'
    >>> simplify(" Washington D.C.\n", delete=",;:.")
    'Washington DC'
    >>> simplify(" disemvoweled ", delete="aeiou")
    'dsmvwld'
    """
    return str1.strip()


def is_included(str1, str2):
    return str1 in str2
