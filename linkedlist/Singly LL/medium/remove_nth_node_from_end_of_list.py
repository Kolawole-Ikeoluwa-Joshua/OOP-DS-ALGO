'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(head, n):
        # add a dummy node to linkedlist with two pointers
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # move second pointer n times
        for i in range(n+1):
            second = second.next


        # move first and second node until second reaches end of linkedlist
        # and first node reaches n-1th node to be deleted
        while second != None:

            first = first.next
            second = second.next


        # remove nth node from linkedlist by updating n-1th next node
        first.next = first.next.next


        # return modified list
        return dummy.next




# create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original DLL:")
curr = head
while curr:
    print(curr.val, end=' ')
    curr = curr.next


# remove nth node from end
ll = Solution.removeNthFromEnd(head=head, n=2)
print()
print()

# print the modified LL
print("Modified LL:")
curr = ll
while curr:
    print(curr.val, end=' ')
    curr = curr.next
        


        