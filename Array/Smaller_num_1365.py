##1 approach
nums = [8,1,2,2,3]
li = []
for i in range(len(nums)):
    count=0
    for e in nums:
        if nums[i] > e:
            count+=1
    li.append(count)
print(li)
## oneliner for above approach
# print([(len([i for i in nums if i < digit])) for digit in nums])

## 2 approach
# temp = sorted(nums)
# mapping = {}
# result = []
# for i in range(len(temp)):
# 	if temp[i] not in mapping:
# 		mapping[temp[i]] = i
# print(mapping)
# for i in nums:
#     result.append(mapping[i])
# print(result)

## 3 approach 
# nums2=sorted(nums)
# dc={item:nums2.index(item) for item in nums2}
# print([dc[item] for item in nums])
