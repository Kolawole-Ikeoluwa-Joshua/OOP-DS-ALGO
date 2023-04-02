'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(head):

        '''
        approach:
        # tortoise and hare algorithm
        # slow starts at head, fast two nodes after
        # The fast pointer moves twice as fast as the slow pointer
        # when fast pointer reaches end of the linked list, the slow pointer will be at the node before middle node
        # then delete the middle node by skipping over it
        # Note: If the linked list has an even number of nodes, we delete the second of the two middle nodes.

        Time: O(n)
        Space: O(1)
        '''
        # code here

        # if it is an empty list
        if not head and not head.next:
            return head

        # if single node linkedlist
        if head and not head.next:
            return None
        
        slow = head
        fast  = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # update list by skipping middle node
        slow.next = slow.next.next

        return head



# create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

# delete the middle node
ll = Solution.deleteMiddle(head=head)

# print the modified LL
print("Modified LL:")
curr = ll
while curr:
    print(curr.val, end=' ')
    curr = curr.next