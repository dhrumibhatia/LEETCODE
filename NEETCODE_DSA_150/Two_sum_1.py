class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {} #key,value

        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num],i]
            else:
                hash_table[num] = i
sol = Solution()
nums = [2,7,11,15]
target = 18
rslt = sol.twoSum(nums,target)
print(rslt)

#2 approach
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(enumerate(nums), key = lambda x: x[1])
        l, r = 0, len(nums) - 1
        while r > l:
            currSum = nums[l][1] + nums[r][1]
            # print(l,r,currSum)
            if currSum == target:
                return [nums[l][0], nums[r][0]]
            elif currSum > target:
                r -= 1
            else:
                l += 1
        return None


#3 approach
def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        if target - n in nums and i != nums.index(target - n):
            return i, nums.index(target - n)


#4 appraoch
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] + nums[x] == target:
                    return [i,x]

#5 approach (two pointer)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r= len(nums)-1
        while l<r:
            if (nums[l]+nums[r]) == target:
                return [l,r]
            r-=1
            if r == l:
                l += 1
                r = len(nums) - 1


