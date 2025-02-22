class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        a = nums[::-1]
        b = a[:k][::-1]
        return b + a[k:][::-1] 

res = Solution()
print(res.rotate([1,2,3,4,5,6,7],3)) # [5,6,7,1,2,3,4]
# time complexity: O(n)
# space complexity: O(n)

# appraoch 2:
#in-place
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

res = Solution()
print(res.rotate([1,2,3,4,5,6,7],3)) # [5,6,7,1,2,3,4]
# time complexity: O(n)
# space complexity: O(1)