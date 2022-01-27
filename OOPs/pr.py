class se(Exception):
    pass

class cal:
    def div(self,a,b):
        c=a//b
        raise se

try:
    c=cal()
    c.div(10,0)
    
except se:
    print("some")

except :
    print('Error')

finally:
    print("finally")



