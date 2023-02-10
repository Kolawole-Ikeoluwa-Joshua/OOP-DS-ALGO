'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

'''
class Solution:
    def setZeroes(self, matrix):
        # code here

        '''
        The code takes in a 2-dimensional matrix of integers and sets all elements in a row and column to 0 if there is a 0 element in that row or column.

        it those this as implemented below:

        
        Time: O(m * n)
        Space: O(1)
        
        '''
        # set first row and column pointers
        fr = False
        fc = False

        # check every element in matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                # if element is 0
                if matrix[i][j] == 0:

                    # check if this 0 is on first row or first column and store this information in variables fr and fc
                    if i == 0:
                        fr = True

                    if j == 0:
                        fc = True

                    # set the corresponding elements in the first row and first column to 0 if current element == 0.
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        #  loops through the rest of the matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # if corresponding elements in the first row or first column == 0. set current element to 0.
                if matrix[0][j] == 0 or matrix[i][0] == 0:

                    matrix[i][j] = 0


        # checks fr and fc == true, then set all elements in the first row and first column to 0.
        if fr:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0


        if fc:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix



ob = Solution()
ans = ob.setZeroes(matrix=[[0,1,2,0], [3,4,5,2], [1,3,1,5]])
print(ans)