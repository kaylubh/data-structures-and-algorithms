from data_structures.linked_list import LinkedList


class Hashtable:
    """
    A hash table implementation that allows storing key-value pairs.

    Attributes:
        size (int): The size of the hash table.
        _buckets (list): The list of buckets used for storing key-value pairs.

    Methods:
        set(key, value): Inserts or updates a key-value pair in the hash table.
        get(key): Retrieves the value associated with the given key.
        has(key): Checks if the given key exists in the hash table.
        keys(): Returns a list of all the keys in the hash table.
        values(): Returns a list of all the values in the hash table.
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):
        """
        Set the value for a given key in the hashtable.

        Args:
            key: The key to set the value for.
            value: The value to be set.

        Returns:
            None
        """

        drop = [key, value]
        index = self._hash(key)
        bucket = self._buckets[index]

        # check for existing key or collision
        if bucket:

            # check for existing key
            current = bucket.head
            while current:
                current_drop = current.value
                if current_drop[0] == key:
                    current_drop[1] = value
                    return
                current = current.next

            # if collision insert to list
            bucket.insert(drop)

        # bucket is empty
        else:

            bucket = LinkedList()
            bucket.insert(drop)
            self._buckets[index] = bucket

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key to search for in the hashtable.

        Returns:
            The value associated with the given key, or None if the key is not found.
        """

        index = self._hash(key)
        bucket = self._buckets[index]

        # check if anything at index
        if bucket is None:
            return None

        # check for key
        current = bucket.head
        while current:
            current_drop = current.value
            if current_drop[0] == key:
                return current_drop[1]
            current = current.next

        # if collision but no matching key
        return None

    def has(self, key):
        """
        Checks if the hashtable contains a specific key.

        Args:
            key: The key to check for in the hashtable.

        Returns:
            True if the key is found in the hashtable, False otherwise.
        """

        index = self._hash(key)
        bucket = self._buckets[index]

        # check keys for match
        if bucket:
            current = bucket.head
            while current:
                current_drop = current.value
                if current_drop[0] == key:
                    return True
                current = current.next

        # default if no matching keys found
        return False

    def keys(self):
        """
        Returns a list of all the keys in the hashtable.
        """

        keys_list = []

        # iterate over buckets and get keys
        for bucket in self._buckets:
            if bucket:
                current = bucket.head
                while current:
                    current_drop = current.value
                    keys_list.append(current_drop[0])
                    current = current.next

        return keys_list

    def values(self):
        """
        Returns a list of all the values stored in the hashtable.
        """

        values_list = []

        # iterate over buckets and get values
        for bucket in self._buckets:
            if bucket:
                current = bucket.head
                while current:
                    current_drop = current.value
                    values_list.append(current_drop[1])
                    current = current.next

        return values_list

    def _hash(self, key):
        """
        Hashes the given key and returns the index in the hashtable.

        Args:
            key (str): The key to be hashed.

        Returns:
            int: The index in the hashtable.

        Raises:
            TypeError: If the key is not a string.
        """

        if type(key) != str:
            raise TypeError('key must be a string')

        index = 0
        for char in key:
            index += ord(char)
        index *= 461
        index = index % self.size

        return index
