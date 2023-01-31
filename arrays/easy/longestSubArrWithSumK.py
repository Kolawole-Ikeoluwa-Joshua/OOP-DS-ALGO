class Solution:
    def longestSubArrWithSumK(self, arr, n, k):

        length = 0
        sum = 0
        m = {} # hash that stores sum of k elements in subarray


        for i in range(n):
            sum += arr[i]
            
            # if sum of subarray elements == k, update length of subarray
            if sum == k:
                length = i+1
                
            '''
            if sum-k is found in hash then there is another subarray
            with sum == k, to get length of current subarray with sum==k. "USE: i - m[sum-k]". 
            '''
            if sum-k in m:
                
                # update length of Longest Sub-Array with sum == k.
                length = max(length, i - m[sum-k])
                
            # if sum not found in hash, update hash with sum
            if sum not in m:
                m[sum] = i
                
                
        return length


ob = Solution()
ans = ob.longestSubArrWithSumK(arr=[10, 5, 2, 7, 1, 9], n=6, k=15)
print(ans)