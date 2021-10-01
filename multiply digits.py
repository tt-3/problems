# https://www.youtube.com/watch?v=Zy9MQZB-fVE

n = int(input())

l = []
if n in range(10):
    print(n+10)

elif n>9:
    for i in range(9,1,-1):
        while(n%i == 0):
            l.append(i)
            n//=i
            
    if(l == []):
        print("Not possible")    
    else:
        for i in l[::-1]:
            print(i,end="")
