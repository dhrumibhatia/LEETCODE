def rearrangeArray(nums):
    pos = [i for i in nums if i > 0]
    neg = [i for i in nums if i < 0]
    result = []
    for i ,v in zip(pos,neg):
        result.extend([i,v])
    return result
nums = [3,1,-2,-5,2,-4]
print(rearrangeArray([-1,1]))