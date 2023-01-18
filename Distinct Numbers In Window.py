from collections import Counter


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        # N = len(A);
        # temp=[]
        # result=[]
        # count = 0;
        # if B > N:
        #     return result
        # for i in range(0,N):
        #     if(i>=B):
        #         tp= temp[0]
        #         temp.pop(0)
        #         result.append(count)
        #         if tp not in temp:
        #             count = count-1
                
            
        #     if A[i] not in temp:
        #         count = count+1
        #     temp.append(A[i])
        #     # print(temp)
        #     # print(count)
            
        # result.append(count)

        # return result
            
        nums= A
        k = B
        c = Counter()
        for i in range(k):
            c[nums[i]] += 1
        ans = []
        for i in range(k, len(nums)):
            ans.append(len(c))
            c[nums[i]] += 1
            c[nums[i - k]] -= 1
            if c[nums[i - k]] == 0:
                del c[nums[i - k]]
        ans.append(len(c))
        return ans

      
'''
Problem Description

You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE:  if B > N, return an empty array.



Input Format
First argument is an integer array A

Second argument is an integer B.



Output Format
Return an integer array.



Example Input
Input 1:

 A = [1, 2, 1, 3, 4, 3]
 B = 3
Input 2:

 A = [1, 1, 2, 2]
 B = 1


Example Output
Output 1:

 [2, 3, 3, 2]
Output 2:

 [1, 1, 1, 1]


Example Explanation
Explanation 1:

 A=[1, 2, 1, 3, 4, 3] and B = 3
 All windows of size B are
 [1, 2, 1]
 [2, 1, 3]
 [1, 3, 4]
 [3, 4, 3]
 So, we return an array [2, 3, 3, 2].
Explanation 2:

 Window size is 1, so the output array is [1, 1, 1, 1].
'''
                
