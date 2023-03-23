'''
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.

'''
# Node definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# deleteNode method
class Solution:
    def deleteNode(node):

        '''
        Time: O(1)
        Space: O(1)
        '''
        # code here

        node.val = node.next.val
        node.next = node.next.next


# Build the LinkedList

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# get node to be deleted
node_to_delete = head.next.next


# delete node
Solution.deleteNode(node_to_delete)


# print linkedlist
current_node = head
while current_node:
    print(current_node.val, end=' ')
    current_node = current_node.next

