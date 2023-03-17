'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 

typically using all the original letters exactly once.
'''


class Solution:
    def isAnagram(self, s, t):

        '''
        Time: O(k*n) == O(n);
        
        k is the number of unique characters in s, where k is constant since at most k = 26
        count method, which takes O(n) time, where n is the length of the input strings

        Space: O(1)
        '''
        # code here

        # check lengths of strings

        if len(s) != len(t):
            return False
        
        # compute frequencies of each character in string s
        for char in set(s):
            # If the frequencies of char in s and t are not equal
            if s.count(char) != t.count(char):
                return False
            
        return True
                        


ob = Solution()
ans = ob.isAnagram(s="anagram", t="nagaram")
print(ans) 