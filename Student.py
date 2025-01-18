import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 300
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.12
        self.gladness -= 3


    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3


    def to_chill(self):
        print("time to rest")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 50


    def to_work(self):
        print("Time to work")
        self.gladness -= 1
        self.money += 100



    def if_alive(self):
        if self.progress <= 0:
            print(f"I should study")
            self.to_study()
        elif self.gladness <= 10:
            print(f"I should rest")
            self.to_sleep()
        elif self.money <= 0:
            print(f"Too little money")
            self.to_work()




    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")
        print(f"Money - {self.money}")

    def life(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.if_alive()

nick = Student("Nick")

for day in range(365):
    if nick.alive == False:
       break
    nick.life(day)