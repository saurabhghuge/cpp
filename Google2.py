# def solution(n, b):
#     #Your code here
#     k =  len(n)
#     id=[]
#     l = n
#     while l not in id:
#         id.append(l)
#         s = sorted(l)
#         x= ''.join(s[::-1])
#         y =''.join(s)
#         if b== 10:
#             z= int(x)-int(y)
#             l=str(z)
#         else:
#             z_10 = int(to_base_10(x,b)) - int(to_base_10(y,b))
#             l = to_base_10(str(z_10),b)
        
#         l = (k-len(l)) * '0' + l
#     return len(id) - id.index(l)
# def to_base_10(n,cb):
#     cb = int(cb)
#     res = 0
#     i = 0
#     while i < len(n):
#         res = (int(n[i]) * (cb ** i)) + res
#         i = i+1
#     return res

def dTob(d, b):
    digits = []
    while d > 0:
        digits.insert(0, str(d % b))
        d  = d / b
    return ''.join(digits)
def bTod(b, c):
  n = 0
  for d in str(b):
    n = c * n + int(d)
  return n
def negative(x, y, b):
  if b==10:
    return int(x) - int(y)
  dx=bTod(x,b)
  dy=bTod(y,b)
  dz=dx-dy
  return dTob(dz, b)
def solution(n, b):
    arr=[]
    while True:
        i = "".join(sorted(str(n), reverse=True))
        j = "".join(sorted(str(n)))
        k = negative(i,j,b)
        k2 = len(str(k))
        i2 = len(str(i))
        if (k2) != i2:
            k = k * pow(10 ,(i2-k2))
        for index, item in enumerate(arr):
          if item == k:
            return index + 1
        arr = [k] + arr
        n = k
n = 210022
b = 3

print(solution(n,b))