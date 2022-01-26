def primesum(A):
    
    isPrime= [0]*(A+1)
    isPrime[0] = isPrime[1]=False
    
    for i in range(2,A+1):
        isPrime[i]= True
    
    p=2
    while(p*p <=A):
        if (isPrime[p]==True):
            i = p*p
            while(i<= A):
                isPrime[i]=False
                i+=p
        p+=1

    for i in range(0,A):
        print(f'{isPrime[i],i} and {isPrime[A-i], A-i}')
        if (isPrime[i] and isPrime[A-i]):

            print(i,(A-i))
            return

primesum(50)