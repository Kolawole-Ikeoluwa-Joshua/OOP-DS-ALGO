'''
Given a linked list of n nodes and a key , the task is to check if the key is present in the linked list or not.

'''
# Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def searchKey(head, key):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here

        if head == None:
            return False
        
        find = Node(key)
        curr = head

        while curr != None:
            if curr.data == find.data:
                return True
            
            curr = curr.next

        return False



# Build the LinkedList

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# print linkedlist
current_node = head
while current_node:
    print(current_node.data, end=' ')
    current_node = current_node.next




# find element in LL
print()
print(Solution.searchKey(head=head, key=4), )