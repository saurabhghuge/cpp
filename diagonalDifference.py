import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum_first_diagonal = sum(arr[i][i] for i in range(n))
    sum_second_diagonal = sum(arr[i][n-i-1] for i in range(n))
    print(str(sum_first_diagonal)+" "+str(sum_second_diagonal))
    return sum_first_diagonal - sum_second_diagonal
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print (result,''
    )
