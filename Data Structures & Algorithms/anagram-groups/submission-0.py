class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word)) # eat -> "a" "e" "t" --join back with--> "".join() --> aet

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())