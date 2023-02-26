'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution:

    '''
    approach: Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:

    - create an array to store spiral elements
    - get the first row
    - rotate remaining rows counter-clockwise


    time: O(n^2)
    space: O(n)
    '''


    # code here
    def spiralOrder(self, matrix):

        # create an array to store spiral
        res = []

        while matrix:
            # get the first row
            res.extend(matrix.pop(0))
            
            # rotate remaining rows counter-clockwise
            # zip(*matrix) transposes the matrix
            # [*zip(*matrix)] packs the transposed matrix back into a list of tuples.
            # [::-1] reverse counter-clockwise
            matrix = [*zip(*matrix)][::-1]

        return res




ob = Solution()
ans = ob.spiralOrder(matrix=[[1,2,3],[4,5,6],[7,8,9]])
print(ans)