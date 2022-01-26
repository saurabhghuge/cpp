def func(A):
    n= len(A)
    result = 0
    even = odd = 0

    for i in range(n):
        if (i%2==0):
            even += A[i]
        else:
            odd +=A[i]

    #got even sums and odd sums

    keven = 0
    kodd = 0
    print(f'{odd} {even}')
    for i in range(n):
        print(f'{keven} {kodd} {result} a[i] {A[i]}')
        if(i%2 == 0):
            
            if((even -(A[i]+keven)+kodd)== ((odd - kodd )+keven)):
                result +=1
            keven += A[i]
        else:
            
            print(f'{odd-(A[i]+kodd)+keven} {odd - keven} {(kodd + (even - keven))}')
            if((odd-(A[i]+kodd)+keven)==(kodd + (even - keven))):
                result +=1
            kodd +=A[i]

    return result

A=[2, 1, 6, 4]
# A = [5, 5, 2, 5, 8]
print(func(A))
