'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 

DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution:

    '''
    approach:
    * clockwise rotate: 
        * first reverse up to down rows, then swap the symmetric elements

    * anti-clockwise rotate: 
        * first reverse left to right columns, then swap the symmetric elements
    
    '''

    # code here
    def rotate(self, matrix):

        matrix.reverse()

        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        return matrix



    def anticlockwise(self, matrix):

        for vi in matrix:
            vi.reverse()


        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        return matrix        






ob = Solution()
ans = ob.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]])
ans2 = ob.anticlockwise(matrix=[[1,2,3],[4,5,6],[7,8,9]])
print(ans)
print(ans2)