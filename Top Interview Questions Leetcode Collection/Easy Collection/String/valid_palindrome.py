class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            a = ''.join(i.lower() for i in s if i.isalnum())
            if a[::-1] == a:
                return True
        return False



# time complexity O(n)
s = '0p' #"A man, a plan, a canal: Panama"
r = Solution().isPalindrome(s)
print(r)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        # Join the filtered characters into a single string
        filtered_str = ''.join(filtered_chars)
        # Check if the filtered string is a palindrome
        return filtered_str == filtered_str[::-1]


# time complexity O(n)
s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))  

s = "race a car"
print(solution.isPalindrome(s))  
