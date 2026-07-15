class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # update i and j pointers
            i = j + 1 # actual word start after #, and j is currently at #
            j = j + 1 + length # to get the full word
            decoded_string.append(s[i:j])
            i = j
        
        return decoded_string