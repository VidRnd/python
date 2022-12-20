class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname=surname
        self.position=position
        self._income={"wage": wage, "bonus": bonus}
class Position(Worker):
   def get_full_name(self):
       return  f'ФИО: {self.surname} {self.surname}\nДолжность: {self.position}'
   def get_total_income(self):
       return  f'Оклад: {self._income["wage"]}\nПремия: {self._income["bonus"]}\n------------\nИтого: {sum(self._income.values())}'

start = Position('Олег','Петров','Менеджер',50000,10000)
print(start.get_full_name())
print(start.get_total_income())