class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(self.brand, "is driving at", self.speed, "km/h")

car1 = Car("Toyota", 120)
car1.drive()

    

    


