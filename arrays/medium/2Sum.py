class Solution:
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
    '''
    def twoSum(self, nums, target):
        # create a hash of numbers in the arrays and their indices
        num_indices = {}

        for i in range(len(nums)):
            # find pair element since xa + xb = target
            # pair m = target - xb
            m = target - nums[i]

            # if pair element in hash, return 2 sum indices
            if m in num_indices:
                return [num_indices[m], i]
            else:
                # add num and index to hash
                num_indices[nums[i]] = i


ob = Solution()
ans = ob.twoSum(nums=[2,7,11,15], target=9)
print(ans)