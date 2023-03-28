'''
Linked List Insertion
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    #Function to insert a node at the beginning of the linked list.

    def insertAtBegining(head,x):
        '''
        Time: O(1)
        Space: O(1)
        '''
        # code here
        temp = Node(x)
        temp.next = head
        head = temp
        return head
    
    #Function to insert a node at the end of the linked list.
    
    def insertAtEnd(head,x):
        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        temp = Node(x)
        
        if head == None:
            return temp
            
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = temp
        return head
    

# Build LL
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# insertions
ans = Solution.insertAtBegining(head=head, x=5)
Solution.insertAtEnd(head=head, x=6)

# print LinkedList
current_node = ans
while current_node:
    print(current_node.data, end=' ')
    current_node = current_node.next