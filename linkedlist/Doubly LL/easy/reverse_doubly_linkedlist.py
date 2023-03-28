'''
Given a doubly linked list of n elements. The task is to reverse the doubly linked list.

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None


def reverseDLL(head):

    '''
    Time: O(n)
    Space: O(1)
    '''
    # code here

    # iterate through the list, swapping the next and prev attributes of each node
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        curr.prev = next

        # update the head pointer of the list to point to the last node
        prev = curr
        curr = next

    # update the head pointer of the list to point to the last node   
    head = prev
    return head





# create a doubly linked list
dll = Node(1)
dll.next = Node(2)
dll.next.prev = dll
dll.next.next = Node(3)
dll.next.next.prev = dll.next
dll.next.next.next = Node(4)
dll.next.next.next.prev = dll.next.next

# print the original DLL

print("Original DLL:")
curr = dll
while curr:
    print(curr.data, end=' ')
    curr = curr.next


# reverse the DLL
dll = reverseDLL(dll)
print()
print()

# print the reversed DLL
print("Reversed DLL:")
curr = dll
while curr:
    print(curr.data, end=' ')
    curr = curr.next