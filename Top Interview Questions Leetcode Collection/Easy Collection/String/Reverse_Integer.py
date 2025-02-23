class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x *= sign
        
        # Reverse the string representation of the number
        reversed_str = str(x)[::-1]
        
        # Remove leading zeros
        reversed_str = reversed_str.lstrip('0')
        
        # Convert back to integer
        reversed_int = int(reversed_str) * sign
        
        # Check for 32-bit overflow
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        return reversed_int

# Example usage:
s = Solution()
print(s.reverse(1230))          # Output: 321
print(s.reverse(-123))          # Output: -321
print(s.reverse(120))           # Output: 21
print(s.reverse(1534236469))    # Output: 0 (since it overflows)


class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = -1 if x < 0 else 1
        x *= sign

        while x:
            ans = ans * 10 + x % 10
            x //= 10

        return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans
s = Solution()
print(s.reverse(1230))          # Output: 321
print(s.reverse(-123))          # Output: -321
print(s.reverse(120))           # Output: 21
print(s.reverse(1534236469))    # Output: 0 (since it overflows)