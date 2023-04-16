'''
You are given a stack St. You have to reverse the stack using recursion.

Example 1:

Input:
St = {3,2,1,7,6}
Output:
{6,7,1,2,3}

'''

class Solution:
    '''
    Normal Recursion causes stack overflow because Large input lead to creation of too many stack frames

    def pop_stack(self, stack, result):
        if not stack:  # base case: the stack is empty
            return result
        else:
            item = stack.pop()  # pop the top item from the stack
            result.append(item)  # add the item to the result
            return self.pop_stack(stack, result)  # recurse with the updated stack and result

    '''        
    #   Tail Recursion - Python interpreter can optimize the function to reuse the same stack frame for each call, rather than creating a new one. 
    # 
    #   Time: O(N)
    #   Space: O(N)        
    
    def tail_rec_pop_stack(self, stack, result):
        if not stack:
            return result
        else:
            item = stack.pop()
            result.append(item)
            return self.tail_rec_pop_stack(stack, result)
            
            
    def reverse(self,st): 
        #code here
        return self.tail_rec_pop_stack(st, [])
        

# Test

ob = Solution()
ans = ob.reverse(st=[3,2,1,7,6])
print(ans)