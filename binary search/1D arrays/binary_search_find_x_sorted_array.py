'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''
'''
bs rule of thumb:

- Include ALL possible answers when initialize lo & hi
- Don't overflow the mid calculation
if array elements even:
mid = lo + (hi - lo) // 2, (lower mid)
mid = lo + (hi - lo + 1) // 2 (upper mid)

- Shrink boundary using a logic that will exclude mid
- Avoid infinity loop by picking the correct mid and shrinking logic
- Always think of the case when there are 2 elements left
'''
class Solution:
    def binarySearch(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if target < nums[mid]:
                hi = mid -1

            else:
                lo = mid

        return lo if nums[lo] == target else -1







ob = Solution()
ans = ob.binarySearch(nums=[-1,0,3,5,9,12], target=9)
print(ans)
