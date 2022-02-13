if __name__ == '__main__':
    n = int(input())
    while n>0:
        a,b = map(int,input().split(" "))
        c = max(a,b)
        d = a + b 
        print(c)
        print(d)
        print(f"{c} {d}")