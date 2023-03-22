'''
Geek loves linked list data structure. Given an array of integer arr of size n, Geek wants to construct the linked list from arr.

Construct the linked list from arr and return the head of the linked list.

'''


'''
Time: O(N)
Space: O(N)
'''
# define a Node class with arrtibutes value and next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# construct LinkedList
class Solution:
    def constructLL(self,arr):
        # create empty head node
        head = Node(None)
        curr = head

        for i in range(len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next

        # return LL head
        return head.next
    

    
ob = Solution()
ans = ob.constructLL(arr=[1,2,3,4,5])
# print constructed LinkedList
while ans:
    print(ans.data, end = ' ')
    ans = ans.next
print()