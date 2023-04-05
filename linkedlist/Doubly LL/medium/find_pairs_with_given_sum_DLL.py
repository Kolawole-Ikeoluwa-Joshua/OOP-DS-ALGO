'''
Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, head, target):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        # create two pointers, one at beginning and at end of DLL

        first = head
        second = head

        while second.next:
            second = second.next

        # initialize list to return pairs

        pairs = []

        # traverse through list from both ends and compare sums

        while first != second and second.next != first:

            pair_sum = first.data + second.data

            # if sum = target
            if pair_sum == target:
                pairs.append((first.data, second.data))
                first = first.next
                second = second.prev

            # if sum < target, move first
            elif pair_sum < target:
                first = first.next


            else:
                second = second.prev


        return pairs



# create a doubly linked list
dll = Node(1)
dll.next = Node(2)
dll.next.prev = dll
dll.next.next = Node(4)
dll.next.next.prev = dll.next
dll.next.next.next = Node(5)
dll.next.next.next.prev = dll.next.next
dll.next.next.next.next = Node(6)
dll.next.next.next.next.prev = dll.next.next.next
dll.next.next.next.next.next = Node(8)
dll.next.next.next.next.next.prev = dll.next.next.next.next
dll.next.next.next.next.next.next = Node(9)
dll.next.next.next.next.next.next.prev = dll.next.next.next.next.next

# print the original DLL

print("Original DLL:")
curr = dll
while curr:
    print(curr.data, end=' ')
    curr = curr.next



ans = Solution().findPairsWithGivenSum(head=dll, target=7)
print()
print()

print("Pair Sum:")
print(ans)