from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(string_to_validate):
    """

    """

    is_balanced = True

    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]

    openers = Stack()

    # iterate through each character in the string to validate
    for char in string_to_validate:

        # character is an opening bracket
        if char in opening_brackets:

            # push it to the openers stack
            openers.push(char)

        # character is a closing bracket
        elif char in closing_brackets:

            # if openers is empty, then matching bracket impossible
            if openers.is_empty() is True:
                is_balanced = False
                return is_balanced

            # index of closing bracket is the same as index of its matching opening bracket
            matching_index = closing_brackets.index(char)
            # pop the next opening bracket for comparison
            current_opener = openers.pop()
            # evaluate if current opening bracket and closing bracket are matching pairs
            is_balanced = is_balanced and (current_opener == opening_brackets[matching_index])

    return is_balanced
