
def partiton(arr,low,high):
    i = low-1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] =arr[j],arr[i]
    
    arr[i+1],arr[high] =arr[high],arr[i+1]
    return i+1


def quicksort(arr,low,high):
    print(f"{arr}  {low} {high}")
    # print(f"  {arr[low]} {arr[high]}")

    if low<high:
        pi = partiton(arr,low,high)

        quicksort(arr,low,pi - 1)
        quicksort(arr,pi+1,high)
    
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def bubble(arr):
#     for i in range(len(arr)-1):
#         swapped = False
#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]= arr[j+1],arr[j]
#                 swapped = True
#                 print(arr)

#         if not swapped:
#             print("helo")
#             return

#  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def mergesort(arr):
#     if len(arr)>1:
#         print()
#         mid = len(arr)//2
#         L = arr[:mid]
        
#         R = arr[mid:]
#         print(arr)
#         print(f"{L} and {R}")
#         mergesort(L)
#         # print(f'passed L with {L}')

#         mergesort(R)
#         # print(f'passed R with {R}')

#         print(f'this is{L} and {R}')
#         i=j=k=0

#         while i < len(L) and j < len(R):
#             # print(f'in {L[i]} and {R[j]}')
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i+=1
            
#             else:
#                 arr[k] = R[j]
#                 j+=1
#             print(f'while{arr}')
#             k+=1
#         print(f'after 1 st while {arr}''')
        
#         while i < len(L):
#             arr[k] = L[i]
#             i+=1
#             k+=1
#         print(f'after 2 st while {arr}''')

#         while j < len(R):
#             arr[k] = R[j]
#             j+=1
#             k +=1        
#         print(f'after 3 st while {arr}''')


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         print(f'now key {arr[i]}')
#         j = i-1

#         while j >= 0 and key < arr[j]:
#             print(f'j is {j} and {arr[j]}')
#             print(arr)
#             arr[j+1] = arr[j]
#             print(f'while {arr}')
#             j-=1
#         arr[j+1] = key
#         print(f'after while {arr}')
        

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def minindex(arr,start,end):
#     min_index= start
    
#     for i in range(start+1 , end):
#         # print(arr[i])
#         if arr[i]< arr [min_index]:
#             min_index = i
#     return min_index

# def selectionSort(arr):
#     n = len(arr)
#     # print(n)

#     for i in range(0,n):
#         min_index= minindex(arr,i,n)
#         print(min_index)

#         if i != min_index:
#             arr[i],arr[min_index] = arr[min_index],arr[i]
#         print(arr)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#HeapSort

# def heapify(arr,n,i):
#     largest = i
#     l = 2* i +1
#     r = 2*i+2

#     if l<n and arr[i]<arr[l]:
#         largest = l
    
#     if r<n and arr[i]< arr[r]:
#         largest= r
    
#     if largest != i:
#         arr[i],arr[largest] == arr[largest],arr[i]

#         heapify(arr,n,largest)


# def heapsort(arr):
#     n = len(arr)

#     for i in range(n//2-1,-1,-1)
#         heapify(arr,n,i)
#     print(arr)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

arr = [50, 23, 9, 18, 61,12,34, 32]
# arr = [50, 23, 9, 18]

print(arr)
n = len(arr)
quicksort(arr,0,n-1)
# bubble(arr)
# mergesort(arr)
# insertionSort(arr)
# selectionSort(arr)
# heapsort(arr)
print(arr)


#Bubble sort



