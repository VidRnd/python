class Stationery:
    def __init__(self,title):
        self.title=title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self,title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашом')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером')

Pen = Pen("красная")
Pencil = Pencil("серый")
Handle = Handle("черный")
Pen.draw()
Pencil.draw()
Handle.draw()
