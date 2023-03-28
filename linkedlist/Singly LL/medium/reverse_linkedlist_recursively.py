'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Recursively

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head):

        '''
        approach:
        keep track of three nodes at a time: the current node, its previous node, and its next node. 
        In this case;  
        head = current node, 
        head.next = next node, 
        head.next.next = previous node.


        Time: O(n)
        Space: O(1)
        '''
        # code here

        # Base case: If the list is empty or has only one node, return the head node.
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        reversed_list = Solution.reverseList(head=head.next)

        # Set the next node's pointer to point to the current node = set previous node
        head.next.next = head

        # Set the current node's pointer to None to terminate the list
        head.next = None

        # Return the reversed list
        return reversed_list





# create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original DLL:")
curr = head
while curr:
    print(curr.val, end=' ')
    curr = curr.next


# reverse the LL
ll = Solution.reverseList(head=head)
print()
print()

# print the reversed LL
print("Reversed LL:")
curr = ll
while curr:
    print(curr.val, end=' ')
    curr = curr.next