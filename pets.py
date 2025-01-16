class cats:
    def __init__(self, name='NONE'):
        self.name = name

class dogs:
    def __init__(self, name='NONE'):
        self.name = name

class me:
    def __init__(self, name=None, height=175):
        self.name = name
        self.height = height
        self.pets = []

    def __str__(self):
        return f"My name is {self.name}, my height is {self.height}"

    def add_pets(self, cat, dog):
           self.pets.append(cat)
           self.pets.append(dog)

    def print_list_of_pets(self):
        print(f"I also have pets. Cat and dog, their names are:")
        for pet in self.pets:
            print(pet.name)



me_child = me(name="Ala")
print(me_child)
nesia = cats(name="Nesia")
spottie = dogs(name="Spottie")
me_child.add_pets(nesia, spottie)
me_child.print_list_of_pets()

