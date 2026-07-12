class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        i = 0
        while i < len(s):
            if (sorted_s[i] != sorted_t[i]):
                return False
            i += 1
        return True