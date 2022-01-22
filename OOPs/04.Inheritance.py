#  i heritance                      Aggregation
# types of interitance  
'''
Single Level 

parent 
  |
  |
  V
child


'''

class shape:
    def __init__(self) -> None:
        print("hi")

    def cal_area(self):
        print("Hello")

class circle(shape):
    pass

c=circle()
c.cal_area()



## ---------------------------------------child class constructor is not there--------------