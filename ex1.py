def find(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    else:
        return"No solution"

nums = [2,7,11,15]
target = 9
print(find(nums,target))
nums = [3,2,4]
target = 6
print(find(nums,target))
nums = [3,3]
target = 6
print(find(nums,target))
nums = [3,3]
target = 7
print(find(nums,target))