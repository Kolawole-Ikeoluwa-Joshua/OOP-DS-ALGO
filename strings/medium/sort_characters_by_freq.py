'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 

The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

'''
# using python's collection class to count freq of each character
from collections import Counter

class Solution:
    def frequencySort(self, s):

        '''
        Time: O(n logn) - sorted function worst-case time complexity of O(nlogn)
        Space: O(n) - where n is length of input string
        '''
        # code here

        # count freq of each character
        char_freq = Counter(s)

        # sort characters based on their frequency in descending order
        sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)

        # return the sorted string based on character frequencies
        sorted_str = ''.join([char * char_freq[char] for char in sorted_chars])

        return sorted_str


ob = Solution()
ans = ob.frequencySort(s="tree")
ans2 = ob.frequencySort(s="cccaaa")
print(ans)
print(ans2) 