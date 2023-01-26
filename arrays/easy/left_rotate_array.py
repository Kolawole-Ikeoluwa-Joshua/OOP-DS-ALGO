class Solution:
    def leftRotate(self, arr, k, n):
        # left rotate
        temp = [0] * n
        
        """
        if "k" exceeds the length of array "n" then the rotation should be kind of cyclic.
        """

        mod = k % n        
        for i in range(0, n):
            temp[i] = arr[(i + mod) % n]

        
        # update arr with rotation
            
        for i in range(n):
            arr[i] = temp[i]
            
        return arr




# test
ob = Solution()
ans = ob.leftRotate(arr=[1, 2, 3, 4, 5, 6, 7], k=4, n=7)
print(ans)
