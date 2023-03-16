'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

'''


class Solution:
    def longestCommonPrefix(self, strs):

        '''
        Time: O(nm) where n is the number of strings in the array and m is the length of the shortest string in the array.
        Space: O(1)

        This is because we iterate over each string in the array and perform a maximum of m comparisons for each string.
        '''
        # code here

        # check if array strs is empty
        if not strs:
            return ""
        
        # make the first word in strs the common prefix
        prefix = strs[0]

        # check if prefix is in remain string in strs array
        for string in strs[1:]:
            # keep editing prefix and comparing with current string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:len(prefix)-1]

                # if prefix becomes an empty string, no common prefix
                if not prefix:
                    return ""
                
        return prefix




ob = Solution()
ans = ob.longestCommonPrefix(strs=["flower","flow","flight"])
print(ans) 