class Road:
    __HEIGT = 5
    __WEIGHT = 25
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def calculation_of_asphalt(self):
       return f'{self._length} м * {self._width} м * {Road.__HEIGT} кг * {Road.__WEIGHT} см = ' \
              f'{int((self._length*self._width*Road.__HEIGT*Road.__WEIGHT)/1000)} т'

start = Road(20,5000)
print(start.calculation_of_asphalt())