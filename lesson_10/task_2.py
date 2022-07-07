from abc import  ABC, abstractmethod

class Clother(ABC):
    rezult = 0

    def __init__(self,param):
        self.param = param
    @property
    @abstractmethod
    def comsuption(self):
        pass
    def __add__(self, other):
        Clother.rezult+=self.comsuption + other.comsuption
        return Costume(0)
    def __str__(self):
        res=Clother.rezult
        Clother.rezult=0
        return f'{res}'
class Coat(Clother):
    @property
    def comsuption(self):
        return  round((self.param/6.5)+0.5)
class Costume(Clother):
    @property
    def comsuption(self):
        return  round((2*self.param+0.3)/100)

coat = Coat(45)
costume = Costume(195)
print(coat+costume+coat)