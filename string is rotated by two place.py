'''
s = 'auiah234$'
#list(map(int,input().split()))
"""for i in range(len(a)):
    print(a[i],end = " ")"""
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:

    print(any(method(c) for c in s))'''
"""
f = 1
n = 3    
for i in range(1,n+1):

    f =  f * i 
    
print(f)"""
"""***********Check if string is rotated by two places *****"""

x = input()
y = input()
def fun(x,y):
    if len(x)!= len(y):
        return 0
    elif x[2:] + x[0:2]== y or y[2:]+y[0:2]==x:
        return 1 
    else:
        return 0

print(fun(x,y))
