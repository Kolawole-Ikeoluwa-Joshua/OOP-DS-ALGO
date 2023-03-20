'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.

Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.

Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.

Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
Change the sign as necessary (from step 2).

If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

Return the integer as the final result.
'''


class Solution:
    def myAtoi(self,s):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here
        # remove leading and trailing white spaces
        s = s.strip()

        # if string is empty
        if not s:
            return 0
        
        # determine if result is - or +
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # get the integer value
        res = 0
        for c in s:
            if not c.isdigit():
                break

            res = res*10 + int(c)


        # append sign
        res *= sign


        # Clamp the integer to the range [-2^31, 2^31 - 1]
        res = max(min(res, 2**31 -1), -2**31)

        return res
        

ob = Solution()
ans = ob.myAtoi(s="4193 with words")
print(ans)