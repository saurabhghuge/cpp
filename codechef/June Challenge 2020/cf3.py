
def fun(N):  
    
    s = [str (x) for x in input().split()]
    # s.append('0')
    # print(s)
    x = 0
    y = 0 
    z = 0
    for j in range(N):
        # print(s[j])
        # if s[j] == "0":
        #     print("YES")
        #     break
        if x == 0 and y == 0 and s[j] != "5":
            return print("NO")

            # print("NO")
            # break
        else:
            if s[j] == "5" :
                x += 1

            elif s[j] == "10":
                if x == 0 :

                    return print("NO")
                else:
                    y += 1 
                    x -=1

            elif s[j] == "15":
                if x < 2 and y == 0:
                    return print("NO")
                elif y > 0 :
                    z +=1
                    y -=1
                else:
                    z+=1
                    x -=2 
    # print(f"{x} {y} {z}")
    return print("YES")
   

if __name__ =="__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        # print(N)
        

        # print(s)
        # t = [(input().strip("").split())]
        fun(N)
        
        


