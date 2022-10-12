class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        result = []
        n = len(A)
        # print(n)
        # print(A[0])
        condition = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count=0
        for i in range(0,n):
            if A[i] in condition :
                count = count + (n-i)
                # for j in range(i,n):
                    # print(A[i:j])
                    # word = A[i:j]
                    # if word not in result:
                    # result.append(word)
        
        return count % 10003     

'''
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
	here number of substrings are 6 and 6 % 10003 = 6.
  '''