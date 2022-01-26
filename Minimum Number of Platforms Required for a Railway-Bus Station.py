# Minimum Number of Platforms Required for a Railway/Bus Station


def fun(arr,dep):
    n = len(arr)
    # n = n/arr[0]
    # arr.sort()
    # dep.sort()
    i =1
    j = 0
    count = 1
    result = 1
    while(i<n and j<n):
        if arr[i] <= dep[j]:
            count +=1
            i +=1
        elif arr[i]>dep[j]:
            count -=1
            j+=1

        if count>result:
            result = count
    print(result)

if __name__ == "__main__": 
    arr = [900, 940, 950, 1100, 1500, 1800] 
    dep = [910, 1200, 1120, 1130, 1900, 2000 ]
    # temp = min(arr)
    # print(temp)
    
    # n = len(arr) 
    # sort(arr)
    fun(arr,dep)
    # print("Minimum difference is", findMinDiff(arr, n, m))