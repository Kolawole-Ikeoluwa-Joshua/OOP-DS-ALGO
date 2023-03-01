'''
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

Time: O(m * log n)
Space: O(1)

'''

class Solution:
    def findPeakGrid(self, mat):

        # find mid column
        startCol = 0
        endCol = len(mat[0])-1

        while startCol <= endCol:
            maxRow  = 0
            midCol = (endCol + startCol)//2

            # find maximum row element on each mid column
            for row in range(len(mat)):
                maxRow = row if mat[row][midCol] >= mat[maxRow][midCol] else maxRow

            
            # compare maxRow element with left and right adjacent elment
            left_bias = midCol-1 >= startCol and mat[maxRow][midCol-1] > mat[maxRow][midCol]
            right_bias = midCol+1 <= endCol and mat[maxRow][midCol+1] > mat[maxRow][midCol]


            # return matrix coordinates for peak element if found

            if not left_bias and not right_bias:
                return [maxRow, midCol]
            
            elif right_bias:
                startCol = midCol + 1
            else:
                endCol = midCol - 1
            
        # if no peak element
        return []




ob = Solution()
ans = ob.findPeakGrid(mat=[[10,20,15],[21,30,14],[7,16,32]])
print(ans)