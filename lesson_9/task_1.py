import time


class TrafficLight:
    color = ""

    def running(self):
        def color_red():
            print("Красный")
            time.sleep(7)

        def color_yellow():
            print("Желтый")
            time.sleep(2)

        def color_green():
            print("Зеленый")
            time.sleep(4)

        if self.color.lower() == 'зеленный':
            color_green()
            color_red()
            color_yellow()
        elif self.color.lower() == 'желтый':
            color_yellow()
            color_green()
            color_red()
        elif self.color.lower() == 'красный':
            color_red()
            color_yellow()
            color_green()
        else:
            print("Такого цвета нет, или проверьте правильность написания цвета")


start = TrafficLight()
TrafficLight.color = "красный"
start.running()

