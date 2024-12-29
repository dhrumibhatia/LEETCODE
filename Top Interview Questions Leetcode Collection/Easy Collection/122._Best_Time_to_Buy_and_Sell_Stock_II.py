class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if prices == sorted(prices,reverse = True):
            return 0
        else:
            c = 0
            for i in range(len(prices)-1):
                    if prices[i] < prices[i+1]:
                        c = c + prices[i+1] - prices[i]
                    else: continue
            return c
            

res = Solution()
print(res.maxProfit([7,1,5,3,6,4])) 
print(res.maxProfit([1,2,3,4,5]))
print(res.maxProfit([7,6,4,3,1]))
print(res.maxProfit([2,1,2,0,1]))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another approach can be with while loop using two pointer.