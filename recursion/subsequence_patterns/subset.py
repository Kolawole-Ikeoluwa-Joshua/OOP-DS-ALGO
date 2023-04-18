'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

'''
class Solution:
    '''
    Time: O(2^n)
    Space: O(n)
    
    '''
    def sub(self, index, arr, length, lt, result):
        if index == length:
            result.append(arr[:])
            return

        # Include the current element
        arr.append(lt[index])
        self.sub(index + 1, arr, length, lt, result)

        # Exclude the current element
        arr.pop()  # Remove the current element from arr
        self.sub(index + 1, arr, length, lt, result)

    def subsets(self, nums):
        result = []
        self.sub(0, [], len(nums), nums, result)
        return result
    

# Test

ob = Solution()
ans = ob.subsets(nums=[1,2,3])

# Output
print(ans)