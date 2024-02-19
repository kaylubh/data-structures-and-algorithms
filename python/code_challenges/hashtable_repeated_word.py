from data_structures.hashtable import Hashtable


def first_repeated_word(string):
    """
    Finds the first repeated word in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The first repeated word found in the string, or None if no repeated word is found.
    """

    words = []
    words_map = Hashtable()

    # create a list of sanitized words
    sanitized_word = ''
    for index, char in enumerate(string):
        if char.isalpha():
            sanitized_word += char.lower()
        elif char == ' ' and sanitized_word:
            words.append(sanitized_word)
            sanitized_word = ''

        if sanitized_word and (index == len(string) - 1): # handles last word
            words.append(sanitized_word)

    # check for repeats
    for word in words:
        if words_map.has(word):
            return word
        words_map.set(word, word)

    # no repeats
    return None
