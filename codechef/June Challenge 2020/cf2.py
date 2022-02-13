
def fun(s):    
    count = 0
    i  = 0

    # print(len(s))
    while(s[i + 1] != "0"):
    # for i in range(len(s)):
        # print(i)
        # print(s[i])
        # print(s[i+1])
        if s[i] == "x" and s[i + 1] == "y":
            
            count +=1
            # print("count incre ")
            # print(count)
            i +=2
            
            # i =+2
        elif s[i] == "y" and s[i + 1] == "x":
            count +=1
            i +=2
        else :
            i +=1
      
        

    print(count) 

        

    

if __name__ =="__main__":
    T = int(input())
    for i in range(T):
        s = list(input().strip())
        # print(s)
        s.append('0')
        s.append('0')

        # print(s)
        # t = [(input().strip("").split())]
        fun(s)
        
        


