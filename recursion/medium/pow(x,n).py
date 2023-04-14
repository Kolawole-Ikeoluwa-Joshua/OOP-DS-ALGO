'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

'''


class Solution:
    def myPow(self, x, n):

        '''
        Time:
        Space:
        '''
        # code here
        # handle negative cases of n
        # If n is negative, we need to compute x^-n, which is equivalent to 1 / x^n.

        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # base case
        if n == 0:
            return 1
        
        # even cases of n
        elif n % 2 == 0:
            y = self.myPow(x, n//2)
            return y * y
        
        # odd cases of n
        else:
            y = self.myPow(x, (n-1)//2)
            return x * y * y

        


ob = Solution()
ans = ob.myPow(x=2, n=2)
print(ans) 