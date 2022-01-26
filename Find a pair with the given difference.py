def fun(arr,n):
    for i in range(len(arr)):
        for j in range(len(arr)):

            if arr[i]-arr[j]==n or arr[j]-arr[i]==n:
                print("haha")
                print(f"{arr[i]} {arr[j]}")
                return



arr= [5, 20, 3, 2,50, 80 ]
n = 78
fun(arr,n)
