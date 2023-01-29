class Solution:
    def missingNumber(self, A, N):

        '''
        A is an array of number from 1 to integer N, find the missing number from array A.
        Note: Dont use sorting
        '''

        # code here

        # create a hash table to store index, if array A elements were in sorted order.

        hash_index = [0] * N

        # traverse through array A and get index of each element, if sorted in increasing order

        for i in range(len(A)):
            element = A[i]
            index = element - 1

            # store element index in hash
            hash_index[index] += 1

        # return element without an index in hash

        for i in range(len(hash_index)):
            if hash_index[i] == 0:
                return i + 1

    
ob = Solution()
ans = ob.missingNumber(A=[2, 5, 3, 1], N=5)
print(ans)


