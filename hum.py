class Human:
    def __init__(self,  name='NONE'):
        self.name = name

class Auto:
    def __init__(self, brand="Zhiguli"):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passenger.append(passenger)

    def print_list_of_passengers(self):
        if self.passenger != []:
            print(f"name of brand {self.brand} and self.passenger are:")
            for pas in self.passenger:
                print(pas.name)
        else:
            print("No passenger")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Merscedes")
car.add_passenger(nick, kate)
car.print_list_of_passengers()
