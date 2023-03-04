'''
Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.
'''

class Solution:
    def median(self, matrix, R, C):

        '''
        The algorithm works by using binary search to find the median value in the matrix
        Time: O(32 * R * log(C))
        Space: O(1)
        
        '''
        # code here

        start_val = 0
        end_val = 2000

        while start_val <= end_val:

            center_val = (start_val + end_val) // 2

            # count the number of elements in the matrix that are less than or equal to the centre_val using binary search.

            count = 0

            n = R * C

            for i in range(R):


                l, h = 0, C - 1

                while l <= h:

                    mid = l + (h-l) // 2

                    if matrix[i][mid] <= center_val:
                        l = mid + 1

                    else:
                        h = mid - 1

                count += l

            #  If this count is greater than n/2 it means that the median must be in the lower half of the search range
            if count > n // 2:
                end_val = center_val - 1

            # median must be in the upper half of the search range    
            else:
                start_val = center_val + 1


        # return median
        return start_val




ob = Solution()
ans = ob.median(matrix=[[1, 3, 5], [2, 6, 9], [3, 6, 9]], R=3, C=3)
print(ans)