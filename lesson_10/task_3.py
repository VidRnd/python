class Cell:
    def __init__(self,nums):
        self.nums = nums
    def make_order(self,rows):
        print("Ячейки по рядам")
        return '\n'.join(["-"*rows for _ in range(self.nums//rows)])+'\n'+'-'*(self.nums%rows)
    def __str__(self):
        return f'{self.nums}'
    def __add__(self, other):
        print("Сложение")
        return Cell(self.nums+other.nums)
    def __sub__(self,other):
        print("Вычитание")
        return Cell(self.nums-other.nums) if self.nums-other.nums>0\
            else "Вторая ячейка больше первой"
    def __mul__(self, other):
        print("Умножение")
        return Cell(self.nums*other.nums)
    def __floordiv__(self, other):
        print("Деление")
        return Cell(self.nums//other.nums)
cell_1 = Cell(23)
cell_2 = Cell(24)
print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_1*cell_2)
print(cell_1//cell_2)
print(cell_2.make_order(7))
