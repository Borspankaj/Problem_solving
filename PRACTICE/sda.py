class A:
    def __init__(self) -> None:
        self.cal(30)
        print(" da ",self.i)

    def cal(self,i):
        self.i=2*i

class B(A):
    def __init__(self) -> None:
        super().__init__()


    def cal(self,i):
        self.i=3*i


b=B()

