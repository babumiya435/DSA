var twoSum = function(nums, target) {
    let n = nums.length;
    // ----------------- brute force approach -------------------------------
    // for(i = 0; i < n; i++){
    //     for(j = i+1; j < n; j++){
    //         if(nums[i] + nums[j] === target){
    //             return [i,j]
    //         }
    //     }
    // }
    // ----------------- two pointer approach -------------------------------
    let original = [...nums];
    nums.sort((a,b)=> a-b)
    let l = 0, r = n-1;
    while(l < r){
        let sum = nums[l] + nums[r];
        if(sum === target){
            if(nums[l] === nums[r]){
                return [original.indexOf(nums[l]), original.lastIndexOf(nums[l])];
            }else {
                return [original.indexOf(nums[l]), original.indexOf(nums[r])];
            }
        }
        if(sum > target){
            r--;
        }else{
            l++
        }
    }

    // ----------------- has map approach -------------------------------
};