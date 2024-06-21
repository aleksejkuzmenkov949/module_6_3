class Vehicle:
    vehicle_type = "none"


class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса
        self.vehicle_type = "SUV"  # Переопределяем vehicle_type
        self.price = 2500000  # Переопределяем price

    def horse_powers(self):
        return 300  # Переопределяем функцию horse_powers


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)



