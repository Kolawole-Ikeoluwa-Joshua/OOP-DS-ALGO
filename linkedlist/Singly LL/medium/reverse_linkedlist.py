'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here

        # iterate through the list, swapping the next to become prev node
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev




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