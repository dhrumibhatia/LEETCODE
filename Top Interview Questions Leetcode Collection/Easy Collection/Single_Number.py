class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            res ^= i  # XOR operation res = res ^ i
        return res

res = Solution().singleNumber([2,2,1])
print(res)

# time complexity: O(n)
# space complexity: O(1)

# apprach 2: Using Hash Table
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in count:
            if count[num] == 1:
                return num

res = Solution().singleNumber([2, 2, 1])
print(res)

# time complexity: O(n)
# space complexity: O(n)