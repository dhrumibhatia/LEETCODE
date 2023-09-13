# 2089. Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [indexx for indexx ,value in enumerate(sorted(nums)) if value == target]