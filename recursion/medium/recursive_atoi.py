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
        Space: O(n)
        '''
        # code here

        """
        Converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
        """
        # Base case: empty string
        if not s:
            return 0

        # Ignore leading whitespace
        if s[0] == ' ':
            return self.myAtoi(s[1:])

        # Check sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Read digits
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                break

        # Convert digits to integer
        if not digits:
            return 0
        num = int(''.join(digits)) * sign

        # Clamp integer to 32-bit signed range
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647

        return num



ob = Solution()
ans = ob.myAtoi(s="4193 with words")
print(ans)