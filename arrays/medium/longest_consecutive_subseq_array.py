'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

'''

class Solution:
    def longestConsecutive(self, nums):
        '''
        two pointer approach

        Time: O(n)
        Space: O(n)
        
        '''
        # converts the input list nums into a set

        nums = set(nums)
        longestConsec = 0

        for x in nums:
            # checks if x - 1 (the number immediately before x) is not in the set nums
            if x-1 not in nums:

                # starts counting the consecutive numbers that follow x in the set. using variable y, while y is still in the set nums.
                y = x+1

                while y in nums:
                    y += 1

                # update longest consecutive number
                # note y-x is the length of the current consecutive sequence of numbers
                longestConsec = max(longestConsec, y-x)

        return longestConsec

    
ob = Solution()
ans = ob.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1])
print(ans)