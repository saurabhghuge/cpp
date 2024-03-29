class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A);

        l=0
        r=n-1
        temp=0
        //abede
        while(l<=r):
            if(A[l]!=A[r]):
                if(r==n-1):
                    l=l+1
                
                r=n-1
                l=temp+1
                temp=l;
            else:
                l=l+1
                r = r-1
        return temp
        
        
  '''
  Problem Description

Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.



Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.



Input Format
First argument is an string A.



Output Format
Return a integer denoting the minimum characters to be appended (insertion at end) to make the string A a palindrome.



Example Input
Input 1:

 A = "abede"
Input 2:

 A = "aabb"


Example Output
Output 1:

 2
Output 2:

 2


Example Explanation
Explanation 1:

 We can make string palindrome as "abedeba" by adding ba at the end of the string.
Explanation 2:

 We can make string palindrome as "aabbaa" by adding aa at the end of the string.
'''
   
