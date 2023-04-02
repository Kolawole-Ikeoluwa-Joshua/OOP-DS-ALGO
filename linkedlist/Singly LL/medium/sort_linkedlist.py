'''
Given the head of a linked list, return the list after sorting it in ascending order.

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):

        '''
        approach: using merge sort

        Time: O(n logn)
        Space: O(1)
        '''
        # code here

        # base case

        if not head or not head.next:
            return head
        
        # split list into two halves

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        mid, slow.next = slow.next, None


        # recursively sort the two halves

        left, right = self.sortList(head), self.sortList(mid)

        # merge the two sorted halves
        # create dummy list to return sorted order
        dummy = ListNode(0)
        curr = dummy
        # sorting
        while left and right:
            
            if left.val < right.val:
                # append to dummy
                curr.next, left = left, left.next
            else:
                curr.next, right = right, right.next

            curr = curr.next
        curr.next = left or right

        # return sorted list head
        return dummy.next



# create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

print("Original DLL:")
curr = head
while curr:
    print(curr.val, end=' ')
    curr = curr.next


# sort LL
sol = Solution()
ll = sol.sortList(head=head)
print()
print()

# print sorted LL
print("Sorted LL:")
curr = ll
while curr:
    print(curr.val, end=' ')
    curr = curr.next