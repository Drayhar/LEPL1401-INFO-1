class Animal:

    def __init__(self, name):
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False

    def sleep(self):
        if self.asleep == True:
            raise RuntimeError
        self.asleep = True

    def wake_up(self):
        if self.asleep == False:
            raise RuntimeError
        self.asleep = False


class Lion(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4

    def roar(self):
        print("ROARRR!!!")


class Owl(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.diurnal = False
        self.nb_legs = 2

    def fly(self):
        pass


class Giraffe(Animal):

    def __init__(self, name, neck_length=2):
        try:
            if neck_length > 0:
                self.neck_length = neck_length
            else:
                raise ValueError
        except:
            raise ValueError
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4


class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)


def create_my_zoo():
    zoo = Zoo()
    zoo.add_animal(Lion("Robert"))
    zoo.add_animal(Owl("michel"))
    zoo.add_animal(Giraffe("Tic"))
    zoo.add_animal(Giraffe("Tac"))
    return zoo
