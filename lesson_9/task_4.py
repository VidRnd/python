from random import choice
import time


class Car:
    direction = ("Повернул на лево", "Повернул на право", "Разворот на 90 гардусов")

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # print(f'{self.name} ')

    def go(self):
        print(f'{self.name} Поехал')

    def stop(self):
        print('Остановился')

    def turn(self):
        print(f'{choice(self.direction)}')

    def show_speed(self):
        return f'Скорость {self.speed} км\ч'


class TownCar(Car):
    def __init__(self, speed, color, name, max_speed, is_police = False):
        """Добавляем параметр максимальаня скорость"""
        super().__init__(speed, color, name, is_police)
        self.max_speed = max_speed

    def show_speed(self):
        return f'Превышение скорости на {self.speed - 60} км\ч' if self.speed > 60 else super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, acceleration_to_100, is_police = False):
        """Добавляем параметр разгод до 100 км\ч"""
        super().__init__(speed, color, name, is_police)
        self.acceleration_to_100 = acceleration_to_100


class WorkCar(Car):
    def __init__(self, speed, color, name, tonnage, is_police = False):
        """Добавляем параметр тоннах """
        super().__init__(speed, color, name, is_police)
        self.tonnage = tonnage

    def show_speed(self):
        return f'Превышение скорости на {self.speed - 40} км\ч' if self.speed > 40 else super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, number_detainees, is_police = True):
        """Добавляем параметр число задержанных """
        super().__init__(speed, color, name, is_police)
        self.number_detainees = number_detainees


TownCar = TownCar(70, "Желтый", "Легковой автомобиль", 120)
SportCar = SportCar(50, "Синий", "Спортивный автомобиль", 4)
WorkCar = WorkCar(45, "Белый", "Рабочий автомобиль", 400)
PoliceCar = PoliceCar(70, "Бело синия", "Полицейский автомобиль", 3)

start_car = (TownCar, SportCar, WorkCar, PoliceCar)
for i in start_car:
    i.go()
    time.sleep(2)
    print(i.show_speed())
    time.sleep(2)
    i.turn()
    time.sleep(2)
    i.stop()
    print("-" * 45)
    time.sleep(10)
