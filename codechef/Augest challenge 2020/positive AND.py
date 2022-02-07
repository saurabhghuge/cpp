# positive AND.py
# cook your dish here

# from itertools import permutations 
# def my_join(tpl):
#     # print(tpl)
#     return (' '.join([str(i) for i in tpl]))


# def func(n):
#     # print(n)
#     # a = []
#     a = list(permutations(range(1, n+1)))
#     print(a)
#     # for l in range(len(a)):
#     for i in range(len(a)):
#         for j in range(0,n-1):
#             # print(f' {a[i][j]} {a[i][j+1]}')
#             if (a[i][j]&a[i][j+1] >0):
#                 if(j+1==n-1):
#                     return(my_join(a[i]))
#                 continue
#                 # print(hhehe)
#             else:
#                 # print("hehe")
#                 break
#     return(-1)
#             # if j<n:    
#             #     break
#             # else:
#             #     return(a[l])
    
# for t in range(1):
#     n = 5
#     print(func(n))
# def permute(nums):
#     result_perms = [[]]
#     for n in nums:
#         new_perms = []
#         for perm in result_perms:
        

#             for i in range(len(perm)+1):
#                 a = perm[:i] + [n] + perm[i:]
#                 print(a)
#                 new_perms.append(perm[i:] + [n] + perm[:i])

#                 for j in range(0,n-1):
#                     # print(f' {a[i][j]} {a[i][j+1]}')
#                     if (a[j]&a[j+1] >0):
#                         if(j+1==n-1):
#                             return(a)
#                         continue
#                         # print(hhehe)
#                     else:
#                         # print("hehe")
#                         break


#                 # print(new_perms)
#                 result_perms = new_perms
#                 # print(result_perms)
#         print(len(result_perms))  
#     return result_perms

# my_nums = [1,2,3,4,5]
# print("Original Cofllection: ",my_nums)
# print("Collection of distinct numbers:\n",permute(my_nums))

# def checkit(a,n):
#     for j in range(0,n-1):

#         print(f' {a[j]} {a[j+1]}')
#         if (a[j] & a[j+1] >0):
#             if(j+1==n-1):
#                 print(a)
#                 print('courh it varaf')
#                 flag= 1
                
#             continue
#             # print(hhehe)
#         else:
#             # print("hehe")
#             break
# def perm(a, flag,k=0):
#     # return(a)
    
#     n = len(a) 
#     if k == len(a):
#         print (a)
#         checkit(a,n)
#         return(a)
#     else:
#         for i in range(k, len(a)):
#             if flag == 1:
#                 break
#             # return(a)
                
#             a[k], a[i] = a[i] ,a[k]
#                 # for j in range(0,n-1):
#                 #     # print(f' {a[i][j]} {a[i][j+1]}')
#                 #     if (a[j]&a[j+1] >0):
#                 #         if(j+1==n-1):
#                 #             return(a)
#                 #         continue
#                 #         # print(hhehe)
#                 #     else:
#                 #         # print("hehe")
#                 #         break
#             perm(a,flag ,k+1)
#             # return(a)
#             a[k], a[i] = a[i], a[k]
#         return(a)
# flag = 0
# a=[1,2,3]
# print(perm(a,flag))

# import copy
# def perm(prefix,rest,x):
    
#     for e in rest:
#         new_rest=copy.copy(rest)
#         new_prefix=copy.copy(prefix)
#         new_prefix.append(e)
#         new_rest.remove(e)
#         if len(new_rest) == 0:
#             a = new_prefix + new_rest
#             n=len(a)
            
#             # print (a)
#             for j in range(0,n-1):
#                 # print(f' {a[i][j]} {a[i][j+1]}')
#                 if (a[j]&a[j+1] >0):
#                     if(j+1==n-1):
#                         x.append(a)
#                         # print(x)
#                         # return(x)
                        
#                     continue
#                     # print(hhehe)
#                 else:
#                     # print("hehe")
#                     break
#             continue
#         # print(x)
#         perm(new_prefix,new_rest,x)
        
        

# # def chekit(a):
# #     n=len(a)
# #     print (a)
# #     for j in range(0,n-1):
# #         # print(f' {a[i][j]} {a[i][j+1]}')
# #         if (a[j]&a[j+1] >0):
# #             if(j+1==n-1):
                
# #                 return(a)
# #             continue
# #             # print(hhehe)
# #         else:
# #             # print("hehe")
# #             break
# # ... 
# x= []
# n = 5
# arr =[]
# for i in range(1,n+1):
#     arr.append(i)
# perm([],arr,x)
# print(x[0])