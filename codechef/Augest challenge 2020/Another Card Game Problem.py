# cook your dish here

def fun(c,r):
    if c < 9 or r  < 9 :
        if r < 9 :
            print(f"{1} {1}")
            return
        elif c < 9 :
            print(f"{0} {1}")
            return
    cx = c//9
    if c%9 !=0 :
        cx = cx + 1
    rx = r//9
    if r % 9 != 0:
        rx = rx +1
    # print(f"{cx} {rx}")
    
    if cx < rx :
        print(f"{0} {cx}")
        return        
    else :
        print(f"{1} {rx}")
        return
for i in range(int(input())):
    c,r = map(int,input().split())
    fun(c,r)
    
            
    