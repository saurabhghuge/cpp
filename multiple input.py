for _ in range(int(input())):
    d={}
    m,n=map(int,input().strip().split(" "))
    for i in range(m):
        u,v=map(int,input().strip().split(" "))
        if( u in d):
            d[u].add(v)
        else:
            d[u]=set([v])
            
    g=0
    h=0
    for i in range(n):
        u,v=map(int,input().strip().split(" "))
        if(u in d):
            g+=1
            if(v in d[u]):
                h+=1
    u,v=map(int,input().strip().split(" "))
    if(u==g):
        if(v==h):
            print("Great")
        else:
            print("Good")
    else:
        print(":(")

///*******************************************************????????????????///////////////////

def find_max(num, max_list):
    if num <= 11:
        max_list[num] = num
        return num
    else:
        if num not in max_list:
            max_list[num] = find_max(
                num//2, max_list) + find_max(num//3, max_list) + find_max(num//4, max_list)
        return max_list[num]

    # return max(num//2+num//3+num//4, num)
max_list = {}
tc = 10
while tc > 0:
    tc = tc - 1
    try:
        n = int(input())
    except:
        break
    print(find_max(n, max_list))
