print("Python - brute force apprach")

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

#print(twoSum([1,2,3,4], 7))

 print("Two Pointer Apprach O(nlogn), O(1)")

def twoSum(self, nums: List[int], target: int) -> List[int]:
        # preserve original array
        original = nums[:]
        n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # two pointers approach
        # sort the array in ASC
        nums.sort()
        # cal length
        n = len(nums)
        # declare & initiaise the l, r pointers
        l = 0
        r = n-1
        # iterate through , r and calculate sum 
        while(l < r):
            # sum1 = nums[l] + nums[l]
            # sum2 = nums[r] + nums[r]
            sum = nums[l] + nums[r]
            # check sum1 == target
            #     true --> return [l,r]
            # if sum1 == target:
            #     return [original.index(nums[l]), original.index(nums[l])]
            # if sum2 == target:
            #     return [original.index(nums[r]), original.index(nums[r])]
            if sum == target:
                if nums[l] == nums[r]:
                    if n == 2:
                        return [l, r]
                    else:
                        return [original.index(nums[l]), n-1-(original[::-1]).index(nums[l])]
                else:
                    return [original.index(nums[l]), original.index(nums[r])]
            # check sum > target
            #     true --> r--
            #     false l++
            if sum > target:
                r = r - 1
            else:
                l = l + 1