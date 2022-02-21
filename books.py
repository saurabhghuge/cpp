n = int(input())
#a = []
b = []
st =" "
for i in range(n):
    lens = int(input())
    a = list(map(int,input().split()))
    #listToStr = " "
    b = []
    #print(listToStr)
    #print(a)
    for l in range(len(a)):
        s = a[l]
        #print(s)
        count = 0
        for o in range(len(a)):
            if a[o] > s:
                count += 1
        b.append(count)
        
        count = str(count)
        #st += count
    listToStr = ' '.join(map(str, b))
    #print(b)
    print(listToStr)

