'''
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

'''


class Solution:
    def beautySum(self,s):

        '''
        Approach:
        - iterating over all substrings of the string s
        - count the frequency of each character in the substring
        - calculate the beauty of the substring
        - add the beauty of the substring to the overall sum

        Time: O(n^3)
        Space: O(1)
        '''
        # code here

        # using nested for loops to iterate over all substrings in s
        res = 0


        # substring start index
        for i in range(len(s)):

            count = [0] * 26        # list to store substring characters frequencies

            # substring end index
            for j in range(i, len(s)):
                # using ASCII values between 0 - 25 == a - z, to update frequency of each character in substring
                count[ord(s[j]) - ord('a')] += 1
                

                # calculate beauty
                # find most freq and least freq characters in substring

                min_val = float('inf')
                max_val = float('-inf')

                # iterate over all possible characters (from 'a' to 'z'), and for each character, we check if it appears in the substring. 
                for k in range(26):
                    if count[k] > 0:
                        # if it does, update most freq and least freq characters in substring
                        min_val = min(min_val, count[k])
                        max_val = max(max_val, count[k])

                # add the beauty of the substring to the overall sum
                res += max_val - min_val

        return res



ob = Solution()
ans = ob.beautySum(s="aabcbaa")
print(ans)