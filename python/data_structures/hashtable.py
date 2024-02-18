from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):
        """

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

        """

    def values(self):
        """

        """

    def _hash(self, key):
        """

        """

        if type(key) != str:
            raise TypeError('key must be a string')

        index = 0
        for char in key:
            index += ord(char)
        index *= 461
        index = index % self.size

        return index
