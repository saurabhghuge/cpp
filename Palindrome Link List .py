# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
		currEle = A
		result = []
		while currEle :
			result.append(currEle.val)
			currEle = currEle.next
			
		N = len(result)//2
		
		Arr = result[:N]
		
		result.reverse()
		
		RevArr= result[:N]

		if(Arr==RevArr):
			return 1
			
		else:
			return 0
    

'''
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''
