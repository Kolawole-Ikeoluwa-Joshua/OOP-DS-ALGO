'''
Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.

'''
# Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# construct DLL
class Solution:
    def constructDLL(self,arr):

        '''
        Time: O(n)
        Space: O(n)
        '''
        # code here
        head = Node(None)
        curr = head

        for i in range(len(arr)):
            curr.next = Node(arr[i])
            curr.prev = curr
            curr = curr.next

        return head.next


ob = Solution()
ans = ob.constructDLL(arr=[1,2,3,4,5])
# print constructed LinkedList
while ans:
    print(ans.data, end = ' ')
    ans = ans.next
print()