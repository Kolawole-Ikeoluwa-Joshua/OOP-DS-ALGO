class Solution:
    def matSearch(self, mat, N, M, X):

        '''
        Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, 
        and a number X is given find whether element X is present in the matrix or not
        '''

        # solution 1
        '''
        time: O(Nlog(M))
        spaceL O(1)
        
        # for each row in matrix, binary search for X
        for i in range(N):
            l = 0
            r = M-1
            mid = 0

            while l <= r:
                mid = (r+l) // 2

                # if X is greater, ignore left half
                if mat[i][mid] < X:
                    l = mid + 1

                # if X is smaller, ignore right half
                elif mat[i][mid] > X:
                    r = mid - 1

                # means X is present at mid
                else:
                    return 1

        return 0
        '''

        # solution 2

        '''
        start from the top right corner of the matrix
        check if element == X and return ;  
        else if element > X, move left and check element;
        else move to new row if element < X
        Stop when search goes out of bounds.

        time: O(N)
        space: O(1)
        '''

        i = 0
        j = M-1

        while i < N and j >= 0:
            if mat[i][j] == X:
                return 1

            elif mat[i][j] > X:
                j -= 1

            else:
                i += 1

        return 0


		    



ob =Solution()
ans = ob.matSearch(mat=[[3, 30, 38], [44, 52, 54], [57, 60, 69]], N=3, M=3, X=62)
print(ans)


