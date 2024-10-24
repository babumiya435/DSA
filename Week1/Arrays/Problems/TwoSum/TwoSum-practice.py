print("Python - brute force apprach")

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

#print(twoSum([1,2,3,4], 7))

 print("Two Pointer Apprach O(nlogn), O(1)")

def twoSum1(nums,target):
    # two pointer apprach
    # calculate length
    n = len(nums)
    # declare and initialise the l, r pointers
    l = 0
    r = n-1
        # iterarte through l, r pointers and caculate sum
    while(l < r):
        sum = nums[l] + nums[r]
        # check sum == target
        # if true return [l,r]
        if(sum == target):
            return [l,r]
        # if false check sum > target
        #     true --> r--
        #     false --> l++ 
        if(sum > target):
            r = r - 1
        else:
            l = 1 + 1
    
print(twoSum1([1,5,3,4], 7));  