from data_structures.hashtable import Hashtable


def left_join(hashmap_a, hashmap_b):
    """

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
