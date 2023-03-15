'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 

The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 

The returned string should only have a single space separating the words. Do not include any extra spaces.
'''
'''
solution 2:

Time: O(n)
Space: O(1)

class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()[::-1]
        s=' '.join(k)
        return s

'''

class Solution:
    def reverseWords(self,s):

        '''
        Time: O(n)
        Space: O(1) each word in string reversed in-place
        '''
        # code here

        # remove leading and trailing spaces
        s = s.strip()

        # reverse the entire string
        s = s[::-1]

        # reverse each word in the string
        start = 0
        for end in range(len(s)):

            # each word ends with a space character
            # at each position check if character == ' '

            if s[end] == ' ':
                # reverse current word in-place
                # concatenate three substrings (the string part before the word, the reversed word, and the part after the word).
                s = s[:start] + s[start:end][::-1] + s[end:]
                start = end + 1


        # Reverse the last word in the string
        # since we might not get to do it in the loop earlier because the last word might not end with a space character

        s = s[:start] + s[start:][::-1]

        # Join the reversed words with a single space
        return ' '.join(s.split())



ob = Solution()
ans = ob.reverseWords(s="the sky is blue")
print(ans) 