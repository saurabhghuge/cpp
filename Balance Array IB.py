class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        
        odd = 0
        even = 0
        for i in range(0,n):
            if (i % 2 ) :
                # print(i)
                even = even + A[i]
            else:
                odd += A[i]
        curr=0
        count=0
        tempeven = 0
        tempodd = 0
        for j in range(0,n):
            curr = A[j]
            if(j % 2):

                if((tempeven+odd)==(tempodd+even-curr)):

                    count = count + 1
                tempeven = tempeven + A[j]
                even = even - curr

            else:
                if((tempeven+odd-curr)==(tempodd+even)):
                    count = count + 1
                tempodd = tempodd + A[j]
                odd = odd - curr
        return count      
        
  
'''
Problem Description

Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the count of special elements.



Example Input
Input 1:

 A = [2, 1, 6, 4]
Input 2:

 A = [5, 5, 2, 5, 8]


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 After deleting 1 from array : {2,6,4}
    (2+4) = (6)
 Hence 1 is the only special element, so count is 1
Explanation 2:

 If we delete A[0] or A[1] , array will be balanced
    (5+5) = (2+8)
 So A[0] and A[1] are special elements, so count is 2.
'''
