class Transport():
    def __init__(self, coordinates, speed, brand, year, number, *args, **kwargs):
        self._coordinates = coordinates  # использование _ перед именем для обозначения "protected" поля
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    def __str__(self):
        '''
        Представление всей информации для вывода в методе print()
        '''
        return f"{self._brand} ({self._year}) - {self._coordinates}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданной области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        x, y = self._coordinates
        return pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width


class Passenger():
    def __init__(self):
        self._passengers_capacity = 0
        self._number_of_passengers = 0

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self):
        self._carrying = 0

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height


class Auto(Transport):
    pass


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port

class Car(Auto):
    pass


class Bus(Auto):
    pass


class CargoAuto(Auto):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship):
    pass


class CargoShip(Ship):
    pass


class Seaplane(Plane, Ship):
    pass

class Seaplane(Plane, Ship, object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Доп. атрибуты для класса Seaplane
        self.floatation_devices = kwargs.get('floatation_devices', 2)

    def takeoff(self):
        print("Seaplane is taking off")








