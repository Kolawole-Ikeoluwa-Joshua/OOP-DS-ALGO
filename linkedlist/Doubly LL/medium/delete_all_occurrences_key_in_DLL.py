'''
You are given the head of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key and return the new DLL.

Note :- There exists atleast 1 distinct element other than key.


'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here

        # if element to delete is at head 

        while head and head.data == x:
            head = head.next

            if head:
                head.prev = None


        # if element in between DLL
        curr = head
        while curr and curr.next:
            if curr.next.data == x:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr

            else:
                curr = curr.next

        
        return head



# create a doubly linked list
dll = Node(2)
dll.next = Node(2)
dll.next.prev = dll
dll.next.next = Node(10)
dll.next.next.prev = dll.next
dll.next.next.next = Node(8)
dll.next.next.next.prev = dll.next.next

# print the original DLL

print("Original DLL:")
curr = dll
while curr:
    print(curr.data, end=' ')
    curr = curr.next



ans = Solution().deleteAllOccurOfX(head=dll, x=2)
print()
print()

# print the modified DLL
print("Modified DLL:")
curr = ans
while curr:
    print(curr.data, end=' ')
    curr = curr.next