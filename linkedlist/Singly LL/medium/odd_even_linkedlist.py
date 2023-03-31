'''
Given the head of a singly linked list, group all the nodes with odd indices together 

followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(head):

        '''
        Time: O(n)
        Space: O(1)
        ''' 
        # code here

        # if single node or empty linkedlist
        if not head or not head.next:
            return head

        # set dummy odd and even head nodes
        odd_head = ListNode(0)
        even_head = ListNode(0)

        odd = odd_head
        even = even_head

        # get even and odd nodes in linkedlist
        index = 1
        curr = head

        while curr:
            # if odd add to dummy odd list
            if index % 2 == 1:
                odd.next = curr
                odd = odd.next

            # else add to dummy even list 
            else:
                even.next = curr
                even = even.next


            curr = curr.next
            index += 1

        # connect grouped odd list to grouped even list
        odd.next = even_head.next
        even.next = None

        return odd_head.next    


# create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original DLL:")
curr = head
while curr:
    print(curr.val, end=' ')
    curr = curr.next


# group LL for odd and even nodes
ll = Solution.oddEvenList(head=head)
print()
print()

# print the grouped LL
print("Grouped LL:")
curr = ll
while curr:
    print(curr.val, end=' ')
    curr = curr.next