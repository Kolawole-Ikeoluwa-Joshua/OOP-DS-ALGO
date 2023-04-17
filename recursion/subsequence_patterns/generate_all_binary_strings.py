'''
Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1.

'''
class Solution:
    '''
    Time Complexity: O(2**N)
    Space: O(N)
    
    '''
    def print_binary(self, n, last_digit):
        if n == 0:
            return [""] # return empty lisy
    
        #  recursively call the function with n-1 and the appropriate value for last_digit
        # If last_digit is 0, we can append either 0 or 1 to the string. 
        # If last_digit is 1, we can only append 0 to the string.
        
        result = [] 
        if last_digit == 0:
            for s in self.print_binary(n-1, 0):
                result.append("0" + s)
            for s in self.print_binary(n-1, 1):
                result.append("1" + s)
        else:
            for s in self.print_binary(n-1, 0):
                result.append("0" + s)
    
        return result    
    
    def generateBinaryStrings(self, n):
        # Code here
        # track of a list of valid binary strings of length n that do not have consecutive 1s.
        
        return self.print_binary(n, 0)
    


#Test
ob = Solution()
ans = ob.generateBinaryStrings(3)

#Output
print(ans)