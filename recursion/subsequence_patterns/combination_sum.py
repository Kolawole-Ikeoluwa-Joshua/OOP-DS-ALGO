'''
Given an array of distinct integers candidates and a target integer target, 

return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
from typing import List

class Solution:
    '''
    Time: O(2^t * k)
    Space: O(k * x)
    
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []


        def findCombination(ind: int, target: int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            # pick candidate at index
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findCombination(ind, target - candidates[ind])
                ds.pop()
            # dont pick same candidate at index
            findCombination(ind + 1, target)
        findCombination(0, target)
        return ans


# Test

if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()