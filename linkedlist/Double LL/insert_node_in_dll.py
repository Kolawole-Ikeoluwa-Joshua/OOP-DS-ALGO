'''
Given a doubly-linked list, a position p, and an integer x. 
The task is to add a new node with value x at the position just after pth node in the doubly linked list.

'''
class Node:
	def __init__(self, data):

		self.data = data
		self.next = None
		self.prev = None

class Solution:
    def addNode(head, p, data):


        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        temp = Node(data)

        if head == None:
            head = temp
            return head
        

        curr = head
        count = 0

        while curr:
            if count == p:
                temp.next = curr.next
                curr.next = temp
                temp.prev = curr

            curr = curr.next
            count += 1

        return head
        