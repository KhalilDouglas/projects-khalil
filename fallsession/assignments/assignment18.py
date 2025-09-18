class Car:
    def __init__(self, color, brand, car_type):
        self.color = color
        self.brand = brand
        self.car_type = car_type
    def describe_car(self):
        print(f"This is a {self.color} {self.brand}, which is a {self.car_type}")

        self.speed = 0
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print("Engine Started!!")
        else:
            print("Engine is already on!")

    def stop_engine(self):
        if self.engine_on:
            self.speed = 0
            self.engine_on = False
            print("Engine stopped.")
        else:
            print("Your engine already stopped")

    def acceleration(self):
        if self.engine_on:
            self.speed += 1
            print(f"Accelerated! Current speed: {self.speed}")
        else:
            print("Your engine is stopped")

first_car = Car("red", "Tesla model 3", "electric")

print(first_car.color)
print(first_car.brand)
print(first_car.car_type)
