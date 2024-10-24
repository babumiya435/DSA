console.log("Brute Force apprach O(n^2)O(nlogn), O(1)");
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
//console.log(twoSum([1,2,3,4], 7));

console.log("Two Pointer Apprach O(nlogn), O(1)");

function twoSum1(nums, target){
    // two pointers approach
    // cal length
    let n = nums.length;
    // sort the array in ASC
    nums.sort((a,b)=> a-b);
    // declare & initialise l, r pointers
    let l = 0, r = n-1;
    while(l , r){
        // iterate throug l<r and calcuate sum
        let sum = nums[l] + nums[r];
        // check for the expected condition met
        // if yes return [l,r]
        if(sum === target){
            return [l,r]
        }
        // if no check for sum > t --> r--, sum < t --> l++
        if(sum > target){
            r--;
        }else{
            l++
        }
    } 
}

console.log(twoSum1([1,2,3,4], 7));