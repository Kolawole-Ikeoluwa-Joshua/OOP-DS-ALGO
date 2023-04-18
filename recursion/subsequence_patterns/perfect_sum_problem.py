'''

Given an array arr[] of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7

'''
class Solution:
    '''
    Time: O(nsum) - as it involves nested loops iterating through n and sum
    Space: O(nsum) - as it uses a 2D array of size (n+1) x (sum+1) to store intermediate results in the dp array.

    Algorithm:

    * Define a class Solution with two methods: count_zeros_till_index and perfectSum.
    * count_zeros_till_index method takes an array (arr) and an index (i) as input and returns the count of zeros in the array till the given index.
    * perfectSum method takes an array (arr), an integer (n) representing the size of the array, and an integer (sum) as input, and returns an integer as output.
    * Initialize a 2D dp array of size (n + 1) x (sum + 1) with all values initialized to 0.
    * Loop through the dp array and initialize the first column (j=0) with the count of zeros till the corresponding index in the input array arr, raised to the power of 2 modulo (10^9 + 7).
    * Loop through the dp array using dynamic programming approach to fill it up.
    * For each cell in the dp array, if the value of arr[i-1] is less than or equal to j, update dp[i][j] as the sum of dp[i-1][j-arr[i-1]] and dp[i-1][j] modulo (10^9 + 7).
    * If arr[i-1] is greater than j, update dp[i][j] as dp[i-1][j] modulo (10^9 + 7).
    * Finally, return dp[n][sum] as the output, which represents the count of subsets of arr that sum up to the given sum.
    '''
    def count_zeros_till_index(self, arr, i):
        count = 0
        for j in range(i):
            if arr[j] == 0:
                count += 1
        return count

    def perfectSum(self, arr, n, sum):
        mod = 10**9 + 7
        dp = [[0] * (sum + 1) for _ in range(n + 1)]

        # Initializing the dp array
        for i in range(n + 1):
            dp[i][0] = pow(2, self.count_zeros_till_index(arr, i), mod)

        # Filling up the dp array using dynamic programming
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]) % mod
                else:
                    dp[i][j] = dp[i - 1][j] % mod

        return dp[n][sum]
    


# Test

ob = Solution()
ans = ob.perfectSum(arr=[2, 3, 5, 6, 8, 10], n=6, sum=10)

# Ouput
print(ans)