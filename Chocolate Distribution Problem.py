# Chocolate Distribution Problem

def sort(a):
    n= len(a)
    for j in range(n-1):
        for i in range(n-j-1):
            if a[i] > a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]

    print(a)
def fun(arr,n,m):
    mindiff = 8888888
    diff=0
    for i in range(n):
        try:
            diff=arr[i+m-1]-arr[i]
        except:
            print(mindiff)
            return
        if mindiff > diff:
            mindiff = diff
if __name__ == "__main__": 
    arr = [12, 4, 7, 9, 2, 23, 25, 41, 
          30, 40, 28, 42, 30, 44, 48,  
          43, 50] 
    m = 7 # Number of students 
    n = len(arr) 
    sort(arr)
    fun(arr,n,m)
    # print("Minimum difference is", findMinDiff(arr, n, m)) 