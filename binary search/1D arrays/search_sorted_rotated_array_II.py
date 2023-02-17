'''
Given a sorted and rotated array A of N elements which is rotated at some point, and may contain duplicates and given an element key. 
Check whether the key exist in the array A or not.
'''

class Solution:
    def searchII(self, nums, target):
        # code here

        '''
        Avg:
        Time: O(log n)
        Space: O(1)

        Worst:
        Time: O(n)
        Space: O(1)
        '''

        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + (r-l) // 2
            # if element is found
            if nums[m] == target:
                return True
            
            # skip duplicate
            while l < m and nums[l] == nums[m]:
                l += 1
            

            # if left half before mid is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # if right half after mid is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False


ob = Solution()
ans = ob.searchII(nums=[5,1,3], target=3)
print(ans)