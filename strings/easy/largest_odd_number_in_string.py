'''
You are given a string num, representing a large integer. 

Return the largest-valued odd integer (as a string) 

that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

'''


class Solution:
    def largestOddNumber(self, num):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here

        # iterate over num from right to left
        for i in range(len(num)-1, -1, -1):

            # check if current character is odd
            if num[i] in {'1', '3', '5', '7', '9'}:

                # return substring of num from the beginning to the current index i, which is the largest odd number that is a non-empty substring of num
                return num[:i+1]

        return ""


ob = Solution()
ans = ob.largestOddNumber(num="52")
print(ans) 