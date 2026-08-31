class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)  # Call parent __init__
        self.model = model

    def car_info(self):
        return f"{self.brand} {self.model} ({self.year})"

car1 = Car("Toyota", 2020, "Corolla")

print(car1.info())
print(car1.car_info())