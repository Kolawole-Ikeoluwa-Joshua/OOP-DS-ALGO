'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. 

Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def modDetectCycle(head):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        # detect cycle in linkedlist
        if not head or not head.next:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            # if cycle
            if slow == fast:
                # Reset slow pointer to head and move both pointers at same pace
                slow = head
                while slow != fast.next:
                    slow = slow.next
                    fast = fast.next
                return slow.val

            slow = slow.next
            fast = fast.next.next

        return None




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

# print start node of loop
ans = Solution.modDetectCycle(head=head)
print(ans)