print("Python - brute force apprach")

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum([1,2,3,4], 7))