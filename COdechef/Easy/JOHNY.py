try:
    for _ in range(int(input())):
        n=int(input())
        songs=list(map(int,input().split()))
        k=int(input())-1
        start,end=0,n-1
        while start!=end:

            if k>(end-start)/2:
                if songs[start]>songs[k]:
                    songs[start],songs[k]=songs[k],songs[start]
                    k=start
                else:
                    start+=1
            else:
                if songs[end]<songs[k]:
                    songs[end],songs[k]=songs[k],songs[end]
                    k=end
                else:
                    end-=1
        print(k+1)

except Exception as e :
    pass




### SECOND APPROACH !! BRUTE FORCE 

try:
    for _ in range(int(input())):
        n=int(input())
        songs=list(map(int,input().split()))
        k=int(input())-1
        val=songs[k-1]

        songs.sort()
        songs.index[val]
        print(k+1)


except Exception as e :
    pass

