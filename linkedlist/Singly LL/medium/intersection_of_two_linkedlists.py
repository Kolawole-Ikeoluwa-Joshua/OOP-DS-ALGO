'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        '''
        Time:
        Space:
        '''
        # code here
        # step 2: get list lengths

        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        # step 3: move longer list until both lists are of equal lengths

        if lenA > lenB:
            for _ in range(lenA-lenB):
                headA = headA.next
        else:
            for _ in range(lenB-lenA):
                headB = headB.next


        # step 4: check nodes in each list until they intersect
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        
        return headA

    # step 1: create a function to get length of lists
    def getLength(self, head):

        length = 0
        while head:
            length += 1
            head = head.next
        return length



# Test case:
# listA: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# listB: 7 -> 8 -> 5 -> 6
# Intersection node: 5

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node7.next = node8
node8.next = node5

sol = Solution()
intersection = sol.getIntersectionNode(node1, node7)
if intersection is not None:
    print(intersection.val)  # expected output: 5
else:
    print("The linked lists do not intersect")