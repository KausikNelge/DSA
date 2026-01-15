
nums =[2,7,11,15]
target = 9
n = target
u = len(nums) - 1
result = 0
        
for i in range(len(nums) ):
   
  if nums[i] and nums[u] > 0:
    nums[u] = i + 1
    result = nums[i] + nums[u]
    if result == target:
      break
    print(result)
     
else:
 nums[i] +=1    
