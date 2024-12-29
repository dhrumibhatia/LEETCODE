# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1 ,len(nums)):
            if nums[l] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

# Time Complexity: O(n)
# Space Complexity: O(1)

reslt = Solution()
print(reslt.removeDuplicates([1,1,2]))

# approach2
class Solution:
    def removeDuplicates(self, nums):
        len_nums = len(nums)
        prev_num = None
        i = 0
        count_uniq_nums = 0
        while (i < len_nums):
            num = nums[i]

            if (prev_num is None or num != prev_num):
                nums[count_uniq_nums] = num
                count_uniq_nums += 1

            prev_num = num
            i += 1

        return count_uniq_nums

# approach3
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        return list(set(nums))