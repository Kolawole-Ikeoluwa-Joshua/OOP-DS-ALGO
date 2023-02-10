'''
Given a matrix of  size n x m. Your task is to make Zeroes, that means in whole matrix when you find a zero, 
convert its upper, lower, left, and right value to zero and make that element the sum of the upper, lower, left and right value.
'''

class Solution:

    '''
    Time: O(n * m)
    Space: O(n * m)
    
    '''
    def MakeZeroes(self, matrix):

        # get array dimensions
        row = len(matrix)
        col = len(matrix[0])

        temp = [[0 for j in range(col)] for i in range(row)]

        # store original matrix in temp matix to prevent its values from being overwritten
        for i in range(row):
            for j in range(col):

                temp [i][j] = matrix[i][j]

        # for each element in array check if the value is 0.

        for i in range(row):
            for j in range(col):
                # if zero, set: up, down, left, right adjacent values in the original matrix to zero
                # sum their previous values in the current position of the zero element in original matrix

                if temp[i][j] == 0:
                    val = 0

                    # up
                    if i-1 >= 0:
                        val += temp[i-1][j]
                        matrix[i-1][j] = 0

                    # left
                    if j-1 >= 0:
                        val += temp[i][j-1]
                        matrix[i][j-1] = 0
                    # down
                    if i+1 < row:
                        val += temp[i+1][j]
                        matrix[i+1][j] = 0

                    # right
                    if j+1 < col:
                        val += temp[i][j+1]
                        matrix[i][j+1] = 0

                    
                    # sum
                    matrix[i][j] = val
        
        return matrix




    

ob = Solution()
ans = ob.MakeZeroes(matrix=[[1, 2, 3, 4],[5, 6, 0, 7],[8, 9, 4, 6],[8, 4, 5, 2]])
print(ans)