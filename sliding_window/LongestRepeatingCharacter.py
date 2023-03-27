# Steps:
#   1. Substring signifies a good candidate for sliding window
#   2. Figure out right and left pointer starting location
#   3. Initialize a hashMap that will keep track of each character's count
#   4. Start iteration, using right pointer location minus left pointer location plus one to figure out length
#   5. When visiting next character, add the value to the hashMap if it doesn't exist, and if it does increment it by one
#   6. 

# Optional efficiency: keep track of max frequency, or the character with the greatest number of occurrences, as that is the only variable that can change in the equation lengthOfWindow - charFrequency <= k and increase maxLength


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1) - max(count.values()) > k: # only hit this condition if you exceed the number of swaps you can make, otherwise you continue to increment the longestPossibleLength result
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res