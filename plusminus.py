
def plusminus(n):
    k=map(int,input().split())
    p=0
    ne=0
    z=0
    for i in k:
        if i>0:
            p+=1
        elif i==0:
            z+=1
        elif i<0:
            ne+=1
    print (round((p/n),3))
    print (round((ne/n),3))
    print (round((z/n),3))
    
n=int(input())
plusminus(n)
