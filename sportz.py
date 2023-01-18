n = 7
for i in range(1,n+1):
    #z=i+1
    for j in range(1,i+2):
        print(j,end="")
    for j in range(1,n-i+2):
        print("*",end="")
        #z-=1
        
    print()
