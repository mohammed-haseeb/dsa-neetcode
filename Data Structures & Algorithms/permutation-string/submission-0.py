class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict, s2_dict = {}, {}
        window_len = len(s1)
        l = 0

        for s in s1:
            s1_dict[s] = s1_dict.get(s, 0) + 1

        for r in range(len(s2)):
            s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1
            
            if r - l + 1 > window_len:
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1
            
            if r - l + 1 == window_len and s1_dict == s2_dict:
                return True
        return False