class Solution:
    # @param A : string
    # @return an integer

    def solve(self, A):
        lst=[]
        res1=""
        res2=""
        i=0
        j=len(A)-1
        while i<=j:
            if A[i]==A[j]:
                i+=1
                j-=1
            else:
                lst.append(i)
                lst.append(j)
                break
        if not lst:
            return 1
        i=lst[0]
        j=lst[1]
        res1 = A[:i]+A[i+1:]
        res2=A[:j]+A[j+1:]

        if res1==res1[::-1]:
            return 1
        elif res2==res2[::-1]:
            return 1
        else:
            return 0


'''
Problem Description

Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

If it is possible then return 1 else return 0.



Problem Constraints
3 <= |A| <= 105

 A[i] is always a lowercase character.



Input Format
First and only argument is an string A.



Output Format
Return 1 if it is possible to convert A to palindrome by removing exactly one character else return 0.



Example Input
Input 1:

 A = "abcba"
Input 2:

 A = "abecbea"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 We can remove character ‘c’ to make string palindrome
Explanation 2:

 It is not possible to make this string palindrome just by removing one character 
'''
