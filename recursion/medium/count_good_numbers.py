'''
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. 

However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

'''
class Solution:

    '''
    Time: O(log n)
    SpaceL O(1)
    
    '''
    # evens  = 0, 2, 4, 6, 8  => 5 evens
    # primes = 2, 3, 5, 7     => 4 primes

    p = 10**9 + 7
    
    # calculating x^y efficiently
    def power(self, x: int, y: int) -> int:
        res = 1
        
        x = x % self.p # Update x if it is more than or equal to p
        if x == 0:
            return 0
        
        while y > 0:
            # If y is odd, multiply x with result
            if y & 1:
                res = (res*x) % self.p
                
            # we have done the odd step if it was odd, now do the even step
            y = y>>1 # dividing y by 2, y>>1 is same as y/2
            x = (x*x) % self.p
        
        return res
    
    def countGoodNumbers(self, n: int) -> int:
        count_of_4s = n // 2
        count_of_5s = n - count_of_4s
        ans = ((self.power(4, count_of_4s) % self.p * self.power(5, count_of_5s) % self.p) % self.p)
        return int(ans)      




ob = Solution()
ans = ob.countGoodNumbers(4)
print(ans) 




























def count_good_strings(n):
    primes = [2, 3, 5, 7]  # List of prime digits
    MOD = 10**9 + 7  # Modulo value
    
    def recursive_count(position, is_even, is_prime, memo):
        # Base case: when all positions have been filled
        if position == n:
            return 1
        
        # Check if result has been computed previously
        if (position, is_even, is_prime) in memo:
            return memo[(position, is_even, is_prime)]
        
        # Initialize count to 0
        count = 0
        
        # If current position is even, the digit must be even
        if is_even:
            for digit in range(0, 10, 2):
                count += recursive_count(position+1, False, is_prime, memo)
        # If current position is odd, the digit must be prime
        else:
            for digit in primes:
                count += recursive_count(position+1, True, True if digit in primes else False, memo)
        
        # Store the result in memo and return count modulo MOD
        memo[(position, is_even, is_prime)] = count % MOD
        return memo[(position, is_even, is_prime)]
    
    # Start the recursive call
    return recursive_count(0, True, False, {})
