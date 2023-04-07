'''
Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

'''
# Node Class
class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        
        left = right = head
        while right:
            # compare left and right nodes, then move to next nodes
            if left.data != right.data:
                left.next = right
                right.prev = left
                left = right
            right = right.next
        left.next = None
        return head
    

# Test cases:


node1 = Node(1)
node2 = Node(1)
node3 = Node(1)
node4 = Node(2)
node5 = Node(3)
node6 = Node(4)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

node4.next = node5
node5.prev = node4

node5.next = node6
node6.prev = node5

head = node1

solution = Solution()
head = solution.removeDuplicates(head)

while head:
    print(head.data, end=' ')
    head = head.next