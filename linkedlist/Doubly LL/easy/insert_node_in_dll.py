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
    def addNode(self, head, p, data):


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


# create a doubly linked list
dll = Node(1)
dll.next = Node(2)
dll.next.prev = dll
dll.next.next = Node(3)
dll.next.next.prev = dll.next
dll.next.next.next = Node(4)
dll.next.next.next.prev = dll.next.next

# print the original DLL

print("Original DLL:")
curr = dll
while curr:
    print(curr.data, end=' ')
    curr = curr.next


# add node in the DLL
sol = Solution()
ans = sol.addNode(head=dll, p=3, data=5)
print()
print()

# print the new DLL
print("New DLL:")
curr = dll
while curr:
    print(curr.data, end=' ')
    curr = curr.next