'''

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def searchInsert(self, nums, target):
        '''
        Time: O(n)
        Space: O(1)
        '''
        
        #code here

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                r = m - 1

            else:
                l = m + 1
        '''
        clever loop terminating condition (<=)
        At crucial point before loop condition fails
        indexes (l, r) = are equal, it could either be the index on the L/R of target
        where... L < (target) < R
        [Note: target isn't in array]
        if at L of target (smaller), start would incr by 1 --> (correct Insert position)
        if at R of target (larger), start would remain unchanged --> (correct Insert position)    
        '''
        return l



ob = Solution()
ans = ob.searchInsert(nums=[1,3,5,6], target=2)
print(ans)