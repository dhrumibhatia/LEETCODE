# 1752 check if array is sorted and rotated 

class Solution:
    def check(self, nums: list[int]) -> bool:
        a = sorted(nums)
        return bool([1 for i in range(len(nums)) if a == nums[-i:] + nums[:-i]])

# Time Complexity: O(N^2 * log N) - Sorting the array takes O(N log N) and checking all rotations takes O(N^2).
# Space Complexity: O(N) - Space used for the sorted array and the list comprehension.

# approach
# for i in range(len(nums)):
#     if ss == nums[-i:] + nums[:-i]:   # ss is sorted array variable
#         print(1)   # bool(1)=True & bool(0)=False
# print(a)

# second approach
# TC = O(N)
class Solution:
    def check(self, nums: list[int]) -> bool:
        cnt = 0
        for i in range(len(nums)): 
            if nums[i-1] > nums[i]: cnt += 1
        return cnt <= 1

# Time Complexity: O(N) - We iterate over the array once.
# Space Complexity: O(1) - No extra space is used except for a few variables.

class Solution:
    def check(self, nums: list[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)): 
            if nums[i-1] > nums[i]: cnt += 1
        return cnt == 0 or cnt == 1 and nums[-1] <= nums[0]

# Time Complexity: O(N) - We iterate over the array once.
# Space Complexity: O(1) - No extra space is used except for a few variables.
