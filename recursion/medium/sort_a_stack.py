'''
Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1
'''

class Solution:
    '''
    merge sort the stack in-place

    Time: O(nlogn)
    Space: O\(n)
    
    '''
    def merge_sort(self, stack):
        if len(stack) > 1:
            mid = len(stack) // 2
            left_half = stack[:mid]
            right_half = stack[mid:]
    
            self.merge_sort(left_half)
            self.merge_sort(right_half)
    
            i = j = k = 0
    
            while i < len(left_half) and j < len(right_half):
                if left_half[i] > right_half[j]:
                    stack[k] = left_half[i]
                    i += 1
                else:
                    stack[k] = right_half[j]
                    j += 1
                k += 1
    
            while i < len(left_half):
                stack[k] = left_half[i]
                i += 1
                k += 1
    
            while j < len(right_half):
                stack[k] = right_half[j]
                j += 1
                k += 1
            
    def sort_stack(self, s):
        self.merge_sort(s)

# Tests
s = [11, 2, 32, 3, 41]
Solution().sort_stack(s)
# Output:
print(s)  
