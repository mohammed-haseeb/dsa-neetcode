class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        left, right = 0, length - 1

        while (left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1