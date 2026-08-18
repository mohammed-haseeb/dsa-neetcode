class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1


            curr_len = r - l + 1
            if curr_len - max(freq.values()) <= k: # implies window is valid
                max_len = max(max_len, curr_len)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return max_len