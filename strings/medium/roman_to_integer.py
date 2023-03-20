'''


'''


class Solution:
    def romanToInt(self,s):

        '''
        Time: O(n)
        Space: O(1)
        '''
        # code here

        # hash table to store integer values of roman numerals

        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0

        # replace special cases in Roman numerals, where a smaller value appears before a larger value and is subtracted from it.
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        # iterate through each character in modified input string
        for char in s:
            result += roman_dict[char]

        return result



ob = Solution()
ans = ob.romanToInt(s="MCMXCIV")
print(ans) 