class Car:
    """Класс информации об автомобиле"""

    def __init__(self, color, count_passenger_seats, is_baby_seat):
        """ Конструктор класса Car

        :param color: Цвет машины
        :type color: str
        :param count_passenger_seats: Количество мест
        :type count_passenger_seats: int
        :param is_baby_seat: Наличие десткого кресла
        :type is_baby_seat: bool
        """
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        info = (f"Машина " + self.color + f" цвета, детское кресло "
                + str(self.is_baby_seat)+f", мест для сидения " + str(self.count_passenger_seats))
        return info


my_car = Car("Red", 5, True)
my_car1 = Car("Blue", 3, False)

# print(my_car1)


class Taxi:
    def __init__(self, cars):
        self.cars = Car()

    def find_car(self, count_passengers:int, is_baby:bool):
        if count_passengers<self.cars.count_passenger_seats:
            return Car

        return 5

mmm=Taxi(my_car)

mmm.find_car(5,True)