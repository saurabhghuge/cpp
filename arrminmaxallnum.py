'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your cod
def my_func(arr,n,min,max):
    #print(arr)
    
    for i in range(n):
        if arr[i] == min:
            if min == max:
                return print("YES")
            
            min+=1
        
        else:
            return print("NO")


if __name__ == "__main__":
     
    n = int(input())
    arr = [int (x) for x in input().split()]
    min = min(arr)
    max = max(arr)
    arr.sort()
    my_func(arr,n,min,max)


            
        
