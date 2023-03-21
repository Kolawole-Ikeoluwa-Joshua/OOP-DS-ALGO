'''
Given a string s, return the longest palindromic substring in s.
'''


class Solution:
    def longestPalindrome(self,s):

        '''
        approach: consider each character in the string as a potential center of a palindrome
        then expand both left and right from that center until the palindrome is no longer valid.
        
        Time: O(N^2)
        Space: O(1)
        '''
        # code here

        # Check for single character palindrome
        n = len(s)
        if n < 2:
            return s
        
        # for each character in s, expand around center until there is no more valid palindrome

        start, end = 0, 0
        for i in range(n):
            len1 = self.expand_around_center(s, i, i) #odd
            len2 = self.expand_around_center(s, i, i+1) #even
            max_len = max(len1, len2)

            # if current palindrome length > previous palindrome length, update start & end
            if max_len > end - start:
                start = i - (max_len-1) // 2    
                end = i + max_len // 2

        return s[start:end+1]    

    # helper function to expand around center
    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return length of valid palindrome found
        return right - left - 1



ob = Solution()
ans = ob.longestPalindrome(s="babad")
print(ans)