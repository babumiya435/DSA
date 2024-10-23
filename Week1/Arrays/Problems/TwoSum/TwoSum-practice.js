console.log("Javascript - brute force apprach");
// brute force approach
function twoSum(nums,target){
    let n = nums.length;
    for(let i = 0; i < n; i++){
        for(let j = i + 1; j < n; j++){
            if(nums[i] + nums[j] === target){
                return [i,j];
            }
        }
    }
}

console.log(twoSum([1,2,3,4], 7));