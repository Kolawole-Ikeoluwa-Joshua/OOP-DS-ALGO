'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
'''


class Solution:
    def rotateString(self, s, goal):

        '''
        Time: O(n^2)
        Space: O(n)
        '''
        # code here

        # check lengths of both strings
        if len(s) != len(goal):
            return False

        # rotate string and check if s == goal
        for i in range(len(s)):
            if s == goal:
                return True
            
            s = s[1:] + s[0]

        return False


ob = Solution()
ans = ob.rotateString(s="abcde", goal="cdeab")
print(ans) 