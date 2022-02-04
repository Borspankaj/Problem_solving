from collections import deque

def truckTour(petrolpumps):
    temp=petrolpumps.copy()
    fuel=0
    q1=deque()
    while petrolpumps:
        val=petrolpumps.pop(0)
        q1.append(val)
        fuel+=val[0]
        fuel-=val[1]
        if fuel<0:
            fuel=0
            while q1:
                petrolpumps.append(q1.pop())
            
    

    return temp.index(q1[0])

print(truckTour([[1,5],[10,3],[3,4]]))
    
    


        