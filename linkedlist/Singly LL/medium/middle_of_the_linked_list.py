'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(head):

        '''
        approach:
        # tortoise and hare algorithm
        # The fast pointer moves twice as fast as the slow pointer
        # when fast pointer reaches end of the linked list, the slow pointer will be at the middle node.

        Time: O(n)
        Space: O(1)
        '''
        # code here
        if not head:
            return None
        
        slow = head
        fast  = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



# create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# find the middle node
middle = Solution.middleNode(head=head)

# print the value of the middle node
print(middle.val)