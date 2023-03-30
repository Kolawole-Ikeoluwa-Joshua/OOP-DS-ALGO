'''
Given a linked list of size N. 

The task is to complete the function countNodesinLoop() that checks whether a given Linked List contains a loop
or not and if the loop is present then return the count of nodes in a loop or else return 0. 

C is the position of the node to which the last node is connected. 

If it is 0 then no loop.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def countNodesinLoop(head):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        # detect cycle in linkedlist
        if not head or not head.next:
            return 0
        
        slow, fast = head, head.next
        while fast and fast.next:
            # if loop in linkedlist
            if slow == fast:

                # find start of loop
                slow = head

                while slow != fast.next:
                    slow = slow.next
                    fast = fast.next

                # if start is found, count nodes in loop
                curr = slow
                count = 1

                while curr.next != slow:
                    count += 1
                    curr = curr.next
                return count
            

            slow = slow.next
            fast = fast.next.next
        return 0



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

# print Length of loop in linkedlist
ans = Solution.countNodesinLoop(head=head)
print(ans) 