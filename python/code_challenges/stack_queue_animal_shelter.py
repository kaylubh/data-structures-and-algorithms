from data_structures.queue import Queue


class AnimalShelter:
    """
    Instantiates an object representation of an animal shelter which instantiates two Queue classes to represent shelters for cats and dogs. Follows FIFO principles. Intended to be used with the Cat and Dog classes.
    """

    def __init__(self):
        self.cats_shelter = Queue()
        self.dogs_shelter = Queue()

    def enqueue(self, animal):
        """
        Checks is the animal object being enqueued is a cat or dog and adds it to the appropriate queue.
        """

        if animal.species == "Cat":
            self.cats_shelter.enqueue(animal)

        if animal.species == "Dog":
            self.dogs_shelter.enqueue(animal)

    def dequeue(self, preference):
        """
        Given a preference of "cat" or "dog", returns a cat or dog object from the appropriate queue according to FIFO principles.
        """

        dequeued_animal = None

        if preference == "cat":
            dequeued_animal = self.cats_shelter.dequeue()

        if preference == "dog":
            dequeued_animal = self.dogs_shelter.dequeue()

        return dequeued_animal

class Animal:
    """
    Instantiates an object representation of an animal. Intended to be used as a base class for the Dog and Cat classes.

    Attributes:
    species (string): __name__ attribute of subclass which instantiates this instance of animal
    name (string): name of the animal
    """

    def __init__(self, name):
        self.species = self.__class__.__name__
        self.name = name or None

    def __str__(self):
        return f"Species: {self.species}, Name: {self.name}"

class Dog(Animal):
    """
    Instantiates an object representation of a dog. Extends the Animal class.
    """

    def __init__(self, name = None):
        super().__init__(name)

class Cat(Animal):
    """
    Instantiates an object representation of a cat. Extends the Animal class.
    """

    def __init__(self, name = None):
        super().__init__(name)
