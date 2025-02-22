class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        jo = ''.join(map(str,digits))
        li = [ int(i) for i in str(int(jo)+1)]
        return li
res = Solution().plusOne([1,2,3])
print(res)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Start from the last digit and move leftwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9, we need an extra digit at the beginning
        return [1] + digits

# Example usage:
res = Solution().plusOne([1, 2, 9])
print(res)  # Output: [1, 3, 0]