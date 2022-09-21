t = int(input())
for x in range(t):
# //  a, b = map(int, input().split())
#   print(a + b)
    n = int(input())
    v = [int (x) for x in input().split()]
    k =  [int (x) for x in input().split()]
    # print(v)
    
    curr = 0
    spill= 0
    for i in range(n):
        curr = curr + k[i]
        if(v[i] < curr):
            spill = spill + curr - v[i]
            curr = v[i]
        
    print(str(curr) + " " + str(spill))
