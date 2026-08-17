class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxlen = 0
        l, r = 0, 0

        while (r < len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxlen = max(maxlen, r - l + 1)
                r += 1
            elif s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
        return maxlen