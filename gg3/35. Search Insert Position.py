nums = [1,3,5,6]
target = 5
def insert():
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    print(len(nums))
