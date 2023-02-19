# Reference: neetcode.io https://www.youtube.com/watch?v=wiGpQwVHdE0&t=380s
# E

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # We only want one set so that our space complexity
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet: # We use a while loop because we want to move the left pointer until the character at the right pointer is no longer in the set. This will allow us to not revisit any character because the substring will start fresh at the moment a duplicate is no longer found. We don't retain the length of the substring in a variable, but use the intrinsic property of the sliding window to calculate the length based on the difference between the right pointer and left pointer, with 1 added due to 0 based indexing
                charSet.remove(s[l]) 
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res