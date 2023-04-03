'''
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. 
The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate 
to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_list(head):
    cur = head
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print()

def segregate(head):
    # count occurance of elements in original linkedlist
    zero, one, two = 0, 0, 0
    cur = head
    while cur is not None:
        if cur.data == 0:
            zero += 1
        elif cur.data == 1:
            one += 1
        else:
            two += 1
        cur = cur.next
    # replace original list with sorted elements
    cur = head
    while cur is not None:
        if zero > 0:
            cur.data = 0
            zero -= 1
        elif one > 0:
            cur.data = 1
            one -= 1
        else:
            cur.data = 2
        cur = cur.next
    
    return head

# Creating a sample linked list with 0s, 1s, and 2s
head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)

# Printing the original linked list
print("Original linked list:")
print_list(head)

# Segregating the linked list using the `segregate` function
head = segregate(head)

# Printing the segregated linked list
print("Segregated linked list:")
print_list(head)
