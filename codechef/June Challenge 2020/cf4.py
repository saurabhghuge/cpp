
def fun(N):  
    
    ts =  N
    js = N 
    s = []
    while(js != 0):
        if (ts % 2 )== 0 and  (js % 2 )== 0:
            ts = ts/2 
            js = js / 2
        elif (ts % 2 ) != 0 and  (js % 2 ) != 0:
            js -=1
        elif (ts % 2 )== 0 and  (js % 2 ) != 0:
            js -=1
        elif (ts % 2 ) != 0 and  (js % 2 )== 0:
            s.append(js)
            js -=1
    print(len(s))
            
if __name__ =="__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        # print(N)
        

        # print(s)
        # t = [(input().strip("").split())]
        fun(N)
        