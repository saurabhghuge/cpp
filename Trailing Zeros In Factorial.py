
def trailingZeroes(A):
    if A<5:
        return 0
    count = 0
    A= A-A%5
    print(A)
    while(A!= 0):
        
        count += A/5
        print(count)
        A/= 5
        print(A)
    print(count)
        # for i in range(0,len(ans)):

trailingZeroes(5)
# trailingZeroes(10)
# trailingZeroes(13)    

