'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. 

Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 

Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(head):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        # if null head or single node in linkedlist return false
        if not head or not head.next:
            return False
        
        # use two pointers
        slow, fast = head, head.next

        while fast and fast.next:

            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next

        return False




# create nodes
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

# connect nodes
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2 # create loop

# test detectCycle Function

ans = Solution.detectCycle(head=head)
print(ans)