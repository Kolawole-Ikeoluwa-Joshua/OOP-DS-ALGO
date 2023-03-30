'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(head):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        # if empty return true

        if not head:
            return True
        
        # find the middle of linkedlist

        slow = fast = head
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # reverse second half of linkedlist
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr


        # compare first and second half of linkedlist
        while prev:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next

        return True



# create nodes
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(1)


# connect nodes
head.next = node1
node1.next = node2
node2.next = node3

# print answer

ans = Solution.isPalindrome(head=head)
print(ans)