'''
You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        '''
        Time: O(max(m, n)), where m and n are the lengths of the input linked lists l1 and l2.
        Space: O(max(m, n)), as we create a new linked list to represent the result, which can have at most max(m, n) + 1 nodes (if there is a carry at the end).
        '''
        # code here
        # creat dummy node for new linkedlist
        dummy = ListNode()
        curr = dummy
        carry = 0 # carry over value after addition of elements from two lists

        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            carry = sum // 10 # carry over value after addition of elements from two lists

            curr.next = ListNode(sum % 10) # value of addition

            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2. next if l2 else None

        return dummy.next # return new head


# Define a function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Test Cases
# Example Test Case

# l1
head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

# l2

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

output = Solution().addTwoNumbers(l1=head1, l2=head2)


# Print the result
print("Result:")
printLinkedList(output)