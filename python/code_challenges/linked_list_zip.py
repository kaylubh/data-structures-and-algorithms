from data_structures.linked_list import LinkedList

def zip_lists(list_a, list_b):
    """
    Zips together two LinkedLists one node at a time starting with list_a. Requires the LinkedList class.

    Parameters:
    list_a (LinkedList object): a LinkedList object, first to be added to new zipped list
    list_a (LinkedList object): a LinkedList object, second to be added to new zipped list

    Returns:
    LinkedList object: a new LinkedList object of the zipped lists
    """

    zipped_list = LinkedList()

    list_a_node = list_a.head
    list_b_node = list_b.head

    while list_a_node or list_b_node:
        if list_a_node:
            zipped_list.append(list_a_node)
            list_a_node = list_a_node.next

        if list_b_node:
            zipped_list.append(list_b_node)
            list_b_node = list_b_node.next

    return zipped_list
