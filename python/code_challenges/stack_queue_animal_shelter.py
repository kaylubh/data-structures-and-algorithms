from data_structures.queue import Queue


class AnimalShelter:
    pass


class Animal:
    """

    """

    def __init__(self, name):
        self.species = self.__class__.__name__
        self.name = name

    def __str__(self):
        return f"Species: {self.species}, Name: {self.name}"

class Dog(Animal):
    """

    """

    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    """

    """

    def __init__(self, name):
        super().__init__(name)
