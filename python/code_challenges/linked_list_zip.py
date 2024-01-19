from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    """

    """

    zipped_list = LinkedList()

    list_a_node = a.head
    list_b_node = b.head

    while list_a_node or list_b_node:
        if list_a_node:
            zipped_list.append(list_a_node)
            list_a_node = list_a_node.next

        if list_b_node:
            zipped_list.append(list_b_node)
            list_b_node = list_b_node.next

    return zipped_list
