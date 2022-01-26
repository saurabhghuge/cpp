# Print a given matrix in spiral form



def fun(a):
    m = len(a)
    n = len(a[0])
    print(f'{m} {n}')

    r = c  = 0

    while(r<m and c < n ):
        for i in range(c,n):
            print(a[r][i],end=" ")
        r +=1

        for i in range(r,m):
            print(a[i][n-1],end =" ")
        n -=1

        if (r<m):
            for i in range(n-1,c-1,-1):
                print(a[m-1][i],end= " ")
            
            m -=1

        if (c<n):
            for i in range(m-1,r-1,-1):
                print(a[i][c],end=" ")
            c +=1
            



a = [
  [1]
]


# ans =1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
fun(a)