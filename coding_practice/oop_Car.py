# create a Car class with the attributes make, model, year
# and describe .

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def describe(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

my_car = Car('Toyota', 'Yaris', 2026)
my_car.describe() 
