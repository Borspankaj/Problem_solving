'''class Dog:
    type='PSIT'

    def __init__(self,name,breed,date) -> None:
        self.name=name
        self.breed=breed
        self.__budday=date

    @classmethod
    def class_method(cls):
        print(cls.type)

    
    @staticmethod
    def details(self):
        print(self.name)
        print(self.breed)
        print(Dog.type)
    def mummy(self):
        print(self.__budday)



apna_dog=Dog('Jarvis','German Shepherd','08-10-2018')
apna_dog.details()
print(apna_dog._Dog__budday)

del apna_dog

apna_dog.details()
'''
from calendar import c


class Mobile:
    def __init__(self,brand,case) -> None:
        self.brand=brand
        self.case=case

    def display(self):
        print(self.case.color)


class Case:
    def __init__(self,color) -> None:
        self.color=color

c1=Case('B')
c2=Case('W')
m1=Mobile('h',c1)
c1.color='G'
m1.display()














'''
class Copy:
    def __init__(self,name,pages,p) -> None:
        self.name=name
        self.pages=pages
        self.puzzle=p

    def set_name(self,name):
        self.name=name


cl=Copy('Navneet',200,3)
cl.set_name('Classmate')

print(cl.name,cl.pages,cl.puzzle)
'''
