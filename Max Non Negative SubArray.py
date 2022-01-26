# Max Non Negative SubArray.py
def maxset(A):
    n = len(A)
    # b = []
    # # c = []
    # start =0
    # end = 0
    # maxsum  = 0
    # sum = 0
    # i = 0
    # A.append(-1)
    # # for i in range(n):
    # while(i<n+1):
    #     if A[i] < 0 :
    #         print(f'enterd herre with{A[i]}')
            
    #         if sum > maxsum :
    #             maxsum = sum
    #             b = []
    #             end = i
    #             print(f' se {start} {end}')
    #             b.extend(A[start:end])
    #             print(f'{b}{maxsum}')
    #         start = i+1
    #         sum = 0
    #         i +=1   
            
    #     else:
    #         sum = sum + A[i]
    #         print(f'{sum}and {maxsum}')
    #         i +=1   

    sum = 0
    start=end= 0
    maxstart= maxend= -1
    maxsum= -9999999999
    for i in range(n):
        # print(f'{start} and {end}')
        if A[i]<0:
            start = i+1
            end = i+1
            sum = 0
        
        else:
            sum = sum +A[i]
            if(sum>maxsum):
                maxstart = start
                maxend = i
                maxsum = sum

            elif(sum == maxsum and(end-start> maxend-maxstart)):
                maxstart = start
                maxend = i
                maxsum=sum
            end+=1

    res= []
    # if maxstart == -1:
    #     return res
    a =  A[maxstart:maxend]
    print(a)
    c =(' '.join(map(str, a)))
    return(c)    
        # if A[i]>=0:
        #     sum = sum + A[i]
        #     end = i +1
        #     if sum > maxsum:
        #         maxstart = start
        #         maxend = end
        #         maxsum = sum

        
        # else :
        #     sum = 0
        #     start = i+1
        #     end = i+1
            
    # a =  A[maxstart:maxend]
    # c =(' '.join(map(str, a)))  
    # # c =str(A[maxstart:maxend]  
    # print(c)
    # print(a)
    # a =( ' '.join(map(str, A[maxstart:maxend]))
    # print(*a)
A =[ 1, 2, 5, -7, 2, 5,-1 ]
print(maxset(A))
