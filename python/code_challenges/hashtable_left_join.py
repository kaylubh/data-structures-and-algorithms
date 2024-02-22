from data_structures.hashtable import Hashtable


def left_join(hashmap_a, hashmap_b):
    """
    Left joins two hashmaps and returns a joined table.

    Args:
        hashmap_a (dict): The first hashmap.
        hashmap_b (dict): The second hashmap.

    Returns:
        list: A list of lists representing the joined table. Each inner list contains the key from hashmap_a, its corresponding value, and the value from hashmap_b if the key exists in hashmap_b, otherwise 'NONE'.
    """

    joined_table = []

    for key, value in hashmap_a.items():
        joined_record = []
        joined_record.append(key)
        joined_record.append(value)

        if key in hashmap_b:
            joined_record.append(hashmap_b[key])
        else:
            joined_record.append('NONE')

        joined_table.append(joined_record)

    return joined_table
