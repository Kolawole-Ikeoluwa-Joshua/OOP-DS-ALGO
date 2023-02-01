'''
function search() which takes two arguments(array A and integer N) and returns the number occurring only once.
'''
class Solution:
    def search(self, A, N):
        # Solution 1
        '''
        Use Xor/Bit Manipulation
        Intuition:
        Xor of any two num gives the difference of bit as 1 and same bit as 0.
        Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
        So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
        Time: O(n)
        Space: O(1)
        '''

        # your code here
        """
        xor = 0
        for i in range(N):
            num = A[i]
            xor ^= num
            
        return xor
        """

        # Solution 2
        '''
        The other way is to maintain a num_frequency dictionary and 
        iterate over it to find which key has exactly 1 frequency and return that key/num.
        Time: O(n) for iterating over the nums array
        Space: O(n) for hashing
        
        '''

        # code here
        num_freq = {}
        
        
        for i in range(N):
            element = A[i]
            
            if element in num_freq:
                num_freq[element] += 1
                
            else:
                num_freq[element] = 1

            
        for element, freq in num_freq.items():
            if freq == 1:
                return element
                
        return None

        


ob = Solution()
ans = ob.search(A=[2, 2, 5, 5, 20, 30, 30], N=7)
print(ans)