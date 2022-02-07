# cook your dish here
# cook your dish here
import math
def fun(h,p):
    while not (h<= 0 or p<= 0):
           
                h = h-p
                p = math.floor(p/2)
                # print(p)
              
 
    if h <= 0 :
        print(1)
    else:
        print(0)
        
    
            
            


n = int(input())

for i in range(n):
    h,p = map(int,input().split())
    fun(h,p)
    