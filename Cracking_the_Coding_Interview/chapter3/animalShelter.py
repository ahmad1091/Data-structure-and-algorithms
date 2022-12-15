# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in LinkedList data structure.

class AnimalShelf:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal: List[int]) -> None:
         if animal[1] == 0:
            self.cats.insert(0,animal[0])
        else:
            self.dogs.insert(0,animal[0])

    def dequeueAny(self) -> List[int]:
        if len(self.cats) == 0:
            return self.dequeueDog()
        if len(self.dogs) == 0:
            return self.dequeueCat()
        return self.dequeueDog() if self.dogs[-1] < self.cats[-1] else self.dequeueCat()

    def dequeueDog(self) -> List[int]:
        return [-1, -1] if len(self.dogs) == 0 else [self.dogs.pop(), 1]

    def dequeueCat(self) -> List[int]: 
        return [-1, -1] if len(self.cats) == 0 else [self.cats.pop(), 0]


    
            