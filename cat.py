import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.hunger = 30
        self.thirst = 25
        self.alive = True

    def to_hunt(self):
        print("Time to have a hunt")
        self.progress += 0.13
        self.gladness -= 4
        self.hunger -= 4
        self.thirst -= 4

    def to_sleep(self):
        print("It's better to sleep")
        self.gladness += 3
        self.thirst -= 1

    def to_play(self):
        print("Time to play")
        self.gladness += 4
        self.hunger -= 3
        self.thirst -= 4
        self.progress -= 0.3

    def to_drink(self):
        print("Time to drink")
        self.thirst += 10


    def to_eat(self):
        print("Time to eat")
        self.hunger += 9

    def if_alive(self):
        if self.progress <= 0:
            print(f"I need to hunt")
            self.to_hunt()
        elif self.gladness <= 5:
            print(f"I should sleep")
            self.to_sleep()
        elif self.hunger <= 5:
            print(f"I need to eat")
            self.to_eat()
        elif self.thirst <= 3:
            print(f"I should drink")
            self.to_drink()


    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")
        print(f"Hunger - {self.hunger}")
        print(f"Thirst - {self.thirst}")

    def life(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_hunt()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.to_eat()
        elif live_cube == 5:
            self.to_drink()
        self.end_of_day()
        self.if_alive()

lily = Cat("Lily")

for day in range(31):
    if lily.alive == False:
       break
    lily.life(day)