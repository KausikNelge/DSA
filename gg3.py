
nums = [-4,-1,0,3,10]
a_pos= []
b_neg = []
for i in range(len(nums)):
    if nums[i] >= 0:
        a_pos.append(nums[i])
    else:
        b_neg.append(nums[i])

print(b_neg)
        