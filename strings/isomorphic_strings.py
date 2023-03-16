'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 

No two characters may map to the same character, but a character may map to itself.

'''


class Solution:
    def isIsomorphic(self,s,t):

        '''
        Time: O(n)
        Space: O(n)
        '''
        # code here

        # check if the lengths of both strings are equal

        if len(s) != len(t):
            return False
        
        # create hash tables to map characters from both strings
        s_map, t_map = {}, {}

        # map each characters from both strings simultaneously
        for i in range(len(s)):
            s_char, t_char = s[i], t [i]

            # if characters have not been mapped already map them
            if s_char not in s_map and t_char not in t_map:
                s_map[s_char], t_map[t_char] = t_char, s_char

            # if character already mapped but values do not correspond with expected character in opposite strings
            elif s_map.get(s_char) != t_char or t_map.get(t_char) != s_char:
                return False
            
        return True




ob = Solution()
ans = ob.isIsomorphic(s="egg", t="add")
print(ans) 