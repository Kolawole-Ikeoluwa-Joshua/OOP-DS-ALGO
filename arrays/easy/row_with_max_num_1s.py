class Solution:
    def rowWithMax1s(self, arr, n , m):
        '''
        Given a boolean 2D array of n x m dimensions where each row is sorted. 
        Find the 0-based index of the first row that has the maximum number of 1's.
        '''

        # brute force code here
        '''
        Time: O(n*m), space: O(n)

        approach: for each row in matrix count number of ones, return index of largest count

        
		row_index = []
		
		for i in range(n):
		    count = 0
		    k = 0
		    while k < m:
		        if arr[i][k] == 1:
		            count += 1
		        k += 1
		    row_index.append(count)
		    
		element = max(row_index)
		if element:
		    return row_index.index(element)
		    
		else:
		    return -1

        
        '''

        # optimal code

        '''
        To solve in O(N + M) start from the top right corner of the matrix and keep 
        Track of the index of the row which has maximum 1s. 
        Go left if you encounter 1
        Go down if you encounter 0
        Stop when you reach the last row or first column. 
        '''

        i = 0
        j = m-1
        ans = -1

        while i < n and j >= 0:
            if arr[i][j] == 1:
                ans = i
                j -= 1

            if arr[i][j] == 0:
                i += 1

        return ans

ob = Solution()
ans = ob.rowWithMax1s(arr=[[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]], n=4, m=4)
print(ans)