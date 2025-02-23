class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        
        return -1
# Time Complexity: O(n^2)
# Example usage:
s = "leetcode"
r = Solution()
print(r.firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(r.firstUniqChar(s))  # Output: 2

s = "aabb"
print(r.firstUniqChar(s))  # Output: -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find the first character with a count of 1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        return -1

# Time Complexity: O(n)
# Example usage:
s = "leetcode"
r = Solution()
print(r.firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(r.firstUniqChar(s))  # Output: 2

s = "aabb"
print(r.firstUniqChar(s))  # Output: -1