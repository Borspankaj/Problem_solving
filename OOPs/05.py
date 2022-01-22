'''from abc import ABCMeta,abstractmethod

class Parent(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.num=5

    @abstractmethod

    def show(self):
        pass


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.__var=10

    def show(self):
        print(self.num)
        print(self.__var)


obj=Child()
obj.show()'''


from re import L


class c:
    def __init__(self,n,m):
        self.n=n
        self.m=m
        

class mo:
    def __init__(self,b):
        self.b=b

    def un(self,co):
        co.color="y"

class co:
    def __init__(self):
        self.color="red"


c('cus1',mo('App')).m.un(co())
print(co().color)



