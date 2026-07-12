class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for val in s:
            s_dict[val] = s_dict.get(val, 0) + 1
        for val in t:
            t_dict[val] = t_dict.get(val, 0) + 1

        return s_dict == t_dict