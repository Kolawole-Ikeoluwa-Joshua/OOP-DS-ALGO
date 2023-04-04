'''

A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.
'''
# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the Solution class
class Solution:
    def addOne(self, head):
        """
        Adds 1 to a number represented as a linked list.
        """
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev

        # Add 1 to the linked list
        carry = 1
        current = head
        while current:
            total = current.val + carry
            carry = total // 10
            current.val = total % 10
            if carry == 0:
                break
            current = current.next

        # Reverse the linked list again
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev

        # Handle the case where carry=1 after adding 1 to linkedlist
        if carry == 1:
            new_head = ListNode(1)
            new_head.next = head
            head = new_head

        return head


# Define a function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Test Cases
# Example Test Case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Print the original linked list
print("Original Linked List:")
printLinkedList(head)

output = Solution().addOne(head=head)


# Print the result
print("Result:")
printLinkedList(output)

