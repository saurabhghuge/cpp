# # Bubble-sort.py
# def performOps(A):
#     m = len(A)
#     n = len(A[0])
#     B = []
#     for i in range(len(A)):
#         B.append([0] * n)
#         for j in range(len(A[i])):
#             B[i][n - 1 - j] = A[i][j]
#     return B

# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# B = performOps(A)
# for i in range(len(B)):
#     for j in range(len(B[i])):
#         print (B[i][j])

# def solve(A, B):
#     print('h')
#     hightemp = -999999999999999
#     temp = 0
#     n = len(A)
#     print(n)
#     k = n
#     s =B

#     for i in range(B+1):
#         j=B-i-1
#         count = 0
#         temp = 0
#         while(count<B):
#             # print(f'{temp} and {A[j]}')
#             temp = temp + A[j]
#             j-=1
#             count += 1
#         # print(temp)
#         if temp > hightemp :
#             hightemp = temp
    
#     return hightemp
        
# # A = [50, 23, 9, 18, 61,12,34, 32]
# # A = [5, -2, 3 , 1, 2]
# A =  [ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ]
# B = 81
# c = solve(A,B)
# print(c)

def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    print(B)
    for i in range(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
        print(B)
    return B

A =[5, 10, 2, 1]
B = performOps(A)
for i in range(len(B)):
    print (B[i])
print(B)