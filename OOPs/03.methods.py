#instance
#static
#class  
#abtract 
from abc import ABC, abstractmethod

class PSIT(ABC):
    def __init__(self,name) -> None:
        self.name=name

    def display(self):                 # instance
        print(self.name)

    @staticmethod                      # decorator
    def information():
        print("PSIT !!!")

    @classmethod                       # decorator
    def info(cls):
        print("This is class method !!! ")

    @abstractmethod
    def GAWD():
        pass
    

    

