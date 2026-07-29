class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        left, right = 0, length - 1
        
        while (left < right):            
            if (s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if (s[left].lower() != s[right].lower()):
                return False

        return True