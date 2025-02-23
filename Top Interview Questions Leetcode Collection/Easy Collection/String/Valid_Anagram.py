class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}

        for char in s:
            char_s[char] = s.count(char)
        
        for char in t:
            char_t[char] = t.count(char)
        return char_s==char_t

# time complexity of O(n^2)
s = Solution()
print(s.isAnagram("anagram", "nagaram"))  
print(s.isAnagram("aa", "a"))         



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the strings are different
        if len(s) != len(t):
            return False
        
        # Create dictionaries to count the frequency of each character
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare the frequency dictionaries
        return count_s == count_t

#  time complexity of O(n)
# Example usage:
s = Solution()
print(s.isAnagram("anagram", "nagaram"))  # Output: True
print(s.isAnagram("aa", "a"))          # Output: False


