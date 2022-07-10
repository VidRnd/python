a = [[5,3,1,6],[4,4,4,5],[9,0,5,0]]
b= [[1,1,1,2],[2,2,2,2],[3,3,3,1]]

class Matrix:
    def __init__(self,lst):
        self.lst=lst
    def __str__(self):
        return  '\n'.join(map(str,self.lst))
    def __add__(self, other):
        c=[]
        for i in range(len(self.lst)):
            c.append([])
            for g in range(len(self.lst[0])):
                c[i].append(self.lst[i][g]+other.lst[i][g])
        return '\n'.join(map(str,c))

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1\n{matrix_1}\n{"-"*25}')
print(f'Matrix 2\n{matrix_2}\n{"-"*25}')
print(f'Matrix 1 + Matrix 2\n{matrix_1+matrix_2}')
