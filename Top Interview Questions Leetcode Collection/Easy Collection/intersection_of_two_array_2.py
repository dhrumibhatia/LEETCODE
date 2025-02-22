class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        li = nums1
        em = []
        for i in nums2:
            if i in li:
                em.append(i)
                li.remove(i)
        return em


res = Solution().intersect([1,2,2,1], [2,2])
res1 = Solution().intersect([4,9,5],[9,4,9,8,4])
print(res,res1)

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1 & c2).elements())
res = Solution().intersect([1,2,2,1], [2,2])
res1 = Solution().intersect([4,9,5],[9,4,9,8,4])
print(res,res1)