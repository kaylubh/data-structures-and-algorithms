from data_structures.queue import Queue


class AnimalShelter:
    """

    """

    def __init__(self):
        self.cats_shelter = Queue()
        self.dogs_shelter = Queue()

    def enqueue(self, animal):
        """

        """

        if animal.species == "Cat":
            self.cats_shelter.enqueue(animal)

        if animal.species == "Dog":
            self.dogs_shelter.enqueue(animal)

    def dequeue(self, preference):
        """

        """

        dequeued_animal = None

        if preference == "cat":
            dequeued_animal = self.cats_shelter.dequeue()

        if preference == "dog":
            dequeued_animal = self.dogs_shelter.dequeue()

        return dequeued_animal

class Animal:
    """

    """

    def __init__(self, name):
        self.species = self.__class__.__name__
        self.name = name or None

    def __str__(self):
        return f"Species: {self.species}, Name: {self.name}"

class Dog(Animal):
    """

    """

    def __init__(self, name = None):
        super().__init__(name)

class Cat(Animal):
    """

    """

    def __init__(self, name = None):
        super().__init__(name)
