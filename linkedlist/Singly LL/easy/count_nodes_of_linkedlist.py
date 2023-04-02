'''
Given a singly linked list. 
The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

'''
# Define the Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define the Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


#  Function to count nodes of linkedlist
class Solution:
    def getCount(self, head_node):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here

        if head_node == None:
            return head_node
        
        curr = head_node
        count = 0

        while curr:
            count += 1
            curr = curr.next
        return count





# Example Usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

sol = Solution()

print("Length of the linked list is:", sol.getCount(linked_list.head))