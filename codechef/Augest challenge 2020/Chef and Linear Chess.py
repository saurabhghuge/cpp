# cook your dish here

def fun (n,k,a):

    ans = -1
    lowest = -1
    templow = -1
    # if k % 2 != 0:
    #     for i in range(len(a)):
    #         if a[i] == 1 :
    #             print(lowest)
    #             return
    
    for i in range(len(a)):
        if k % a[i] == 0 :
            templow = k / a[i]
            templow = templow -1
            
            
            # print(f"{templow}  {ans}")
        else :
            continue
        
        if templow != -1 :
            if lowest == -1:
                lowest = templow
                ans = a[i]

            elif lowest > templow:
                lowest = templow
                ans = a[i]
        
            
    
    # print(lowest)   
    print(ans)



for i in range(int(input())):
    n,k = map(int,input().split())
    a =   [int (x) for x in input().split()]
    # print(a)
    fun(n,k,a)