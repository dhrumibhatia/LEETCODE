class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]
s = ["h","e","l","l","o"]
re = Solution().reverseString(s)
print(re)


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            print(s[left], s[right] )
            s[left], s[right] = s[right], s[left]
            print(s[left], s[right] )
            left += 1
            right -= 1
            print(s)
s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)  # Output should be ['o', 'l', 'l', 'e', 'h']