







# if __name__ == "__main__":
#     #T = int(input())
#    # s= []
    
#     #for i in range(0,T):
#         N,M,Q= map(int,input().split())
#         print(N,M,Q)
#         s = []
#         for j in range(Q):
            
#            s.append(input().split())
#             #print(p,k)
#            # l = [p,k]
#             #j[].append(l
        
#         #print(j)
#         print(s)
#         print(s[1][1])
# 
# 
# 
# n=int(input())
# mylist=list(map(int,input().split()))

# for i in range(n//2):
#     if(mylist[0]<mylist[-1]):
#         mylist.remove(mylist[0])
        
#     if(mylist[-1]<mylist[0]):
#         mylist.remove(mylist[-1])

# if(len(mylist)<=1):
#     print('yes')
# else:
#     print('no')     
# 

def remove3ConsecutiveDuplicates(string,n): 
    val = "" 
    i = 0
    while (i < len(string)): 
        if (i < len(string) - 2 and
            string[i] * n == string[i:i + n]): 
            i += n
        else: 
            val += string[i] 
            i += 1
              
    if (len(val) == len(string)): 
        return val 
    else: 
        return remove3ConsecutiveDuplicates(val,n) 
        
s,n= map(str,input().split())  
n = int(n)
val = remove3ConsecutiveDuplicates(s,n) 
print(val)   
# Driver code  

