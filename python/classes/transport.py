from abc import ABC, abstractmethod


class Water(ABC):
    @abstractmethod
    def move(self):
        print("move on water")


class Ground(ABC):
    @abstractmethod
    def move(self):
        print("move on ground")


class Air(ABC):
    @abstractmethod
    def move(self):
        print("move on air")


class Validator:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(
                print(f"{self.name} can't be negative")
            )
        else:
            instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Transport:
    speed = Validator()
    power_reserve = Validator()
    TOTAL_TRANSPORT = 0

    def __init__(self, name='', max_speed=100, power_reserve=200):
        self.name = name
        self.speed = 0
        self.max_speed = max_speed
        self.power_reserve = power_reserve
        Transport.TOTAL_TRANSPORT += 1

    @classmethod
    def how_many(cls):
        print("Total transport units: ", cls.TOTAL_TRANSPORT)

    def __str__(self):
        return(f"{self.name}: \n"
               f" - power reserve: {self.power_reserve}\n"
               f" - max speed: {self.max_speed}\n"
               f" - speed: {self.speed}\n")

    def __add__(self, other):
        if not isinstance(other, Transport):
            speed = int(other)
            other = Transport()
            other.speed = speed

        self.speed = self.speed + other.speed
        return self

    def __gt__(self, other):
        if not isinstance(other, Transport):
            other = Transport(other)
        if self.speed > other.speed:
            return True
        else:
            return False


class Wheel:
    wheel_quantity = Validator()

    def __init__(self, wheel_quantity=4):
        self.wheel_quantity = wheel_quantity

    @property
    def wheel_quantity(self):
        print("Counting wheels...")
        return self._wheel_quantity

    @wheel_quantity.setter
    def wheel_quantity(self, value):
        print("Mounting wheels...")
        if value < 1:
            raise ValueError("You need more wheels than 0")
        self._wheel_quantity = value


class GroundTransport(Transport, Ground, Wheel):
    quantity = 0

    def __init__(self, name='', max_speed=100,
                 power_reserve=200, wheel_quantity=4):
        super().__init__(name, max_speed, power_reserve)
        self.wheel_quantity = wheel_quantity
        GroundTransport.quantity += 1

    @staticmethod
    def how_many():
        print(f'There are {GroundTransport.quantity} units of ground transport'
              )

    def move(self):
        super().move()


class AirTransport(Transport, Air):
    def __init__(self, name='', max_speed=100,
                 power_reserve=200):
        super().__init__(name, max_speed, power_reserve)

    def move(self):
        super().move()


class WaterTransport(Transport, Water):
    def move(self):
        super().move()


truck = GroundTransport('Truck', 140, 499)
bus = GroundTransport('Bus', 90, 350)
bicykle = GroundTransport('Bicykle', 20, 50, 2)
ground_transport = [truck, bus, bicykle]

GroundTransport.how_many()
print()
print(f"{truck}")
print(f"{bus}")
print(f"{bicykle}")
print()
print(f"{truck.name} wheel quantity: {truck.wheel_quantity}")
truck.wheel_quantity = 8
print(f"{truck.name} wheel quantity: {truck.wheel_quantity}")
truck.move()
print()

print(bus)
print(f"Changing bus speed on 90")
bus.speed = 90
print(f"Bus speed: {bus.speed}",)
print()

print(bicykle)
print(f"Changing bicycle speed on 4")
bicykle.speed = 4
print(f"Bicycle speed: {bicykle.speed}")
print()

print(f"Increasing bus speed: bus = bus + 11")
bus = bus + 11
print(f"Bus speed: {bus.speed}")
print()

print("Changing truck: truck.speed += 98")
truck.speed += 98
print(f"Truck speed: {truck.speed}")
print(f"Bus speed: {bus.speed}")
print()
print(f"Is Truck speed bigger then bus speed?: truck > bus : {truck > bus}")
print()

plane = AirTransport('Airbus A380', 1020, 15200)
print(plane)

Transport.how_many()

