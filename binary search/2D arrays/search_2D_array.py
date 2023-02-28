'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Space: O(1)


'''
class Solution:
    def searchMatrix(self, matrix, target):

        row, cols = len(matrix), len(matrix[0])
        l, r = 0, row * cols-1

        while l <= r:
            m = (l + r) // 2

            num = matrix[m // cols][m % cols]

            if num == target:
                return True
            
            elif num < target:
                l = m + 1

            else:
                r = m - 1

        return False


ob = Solution()
ans = ob.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=99)
print(ans)