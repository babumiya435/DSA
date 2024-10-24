class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # ---------------- brute force approach ----------------------------
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # ---------------- two pointers approach ----------------------------
        # preserve original array
        # original = nums[:]
        # sort the array in ASC
        # nums.sort()
        # cal length
        # declare & initiaise the l, r pointers
        # l = 0
        # r = n-1
        # # iterate through , r and calculate sum 
        # while(l < r):
        #     # sum1 = nums[l] + nums[l]
        #     # sum2 = nums[r] + nums[r]
        #     sum3 = nums[l] + nums[r]
        #     # check sum1 == target
        #     #     true --> return [l,r]
        #     # if sum1 == target:
        #     #     return [original.index(nums[l]), original.index(nums[l])]
        #     # if sum2 == target:
        #     #     return [original.index(nums[r]), original.index(nums[r])]
        #     if sum3 == target:
        #         if nums[l] == nums[r]:
        #             return [original.index(nums[l]), n-1-(original[::-1]).index(nums[l])]
        #         else:
        #             return [original.index(nums[l]), original.index(nums[r])]
        #     # check sum > target
        #     #     true --> r--
        #     #     false l++
        #     if sum3 > target:
        #         r = r - 1
        #     else:
        #         l = l + 1
        # ---------------- hash map approach ----------------------------
        # create a empty map
        map = {}
        # iterate through nums array
        # check for target-current value exists in map
        #     - yes --> return map[target-current, current] indices
        #     - no --> insert the item {currentvalue:index} to the map
        for i in range(n):
            if (target - nums[i]) in map:
                return [map[target-nums[i]], i]
            else:
                map[nums[i]] = i 
        