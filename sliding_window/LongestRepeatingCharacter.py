# Steps:
#   1. Substring signifies a good candidate for sliding window
#   2. Figure out right and left pointer starting location
#   3. Initialize a hashMap that will keep track of each character's count
#   4. Start iteration, determine if storing length is necessary or if you can infer length based on right and left pointer locations
#   5.  


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res