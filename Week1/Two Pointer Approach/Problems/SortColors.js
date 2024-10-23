var sortColors = function(nums) {
    //nums.sort((a,b)=> a-b);
    let n = nums.length;
    let l = 0, r = n-1;
    // console.log(l,r)
    if(n <= 1) return nums;
    let xor = 0;
    for(let i = 0; i < n; i++){
        xor = xor ^ nums[i];
    }
    
    if(xor === 0) return nums;
    console.log("after xor", xor, nums[0])
    while(l < r) {
        while(nums[l] === 0){
            l++;
        }
        while(nums[r] === 2){
            r--;
        }
        // if(nums[l] === 0){
        //     l++;
        // }
        // if(nums[r] === 2){
        //     r--;
        // }
        // console.log("before swap 1",nums);
        if( l < r && nums[l] > nums[r]){
            [nums[l], nums[r]] = [nums[r], nums[l]];
            // if(nums[l] === 0){
            //     l++;
            // }
            // if(nums[r] === 2){
            //     r--;
            // }
            // console.log("afetr swap 2",nums);
        } else if(l<r && nums[l] === nums[r]){
            while(l < r){
                if(nums[l+1] === nums[l]) l++;
                if(nums[r] === nums[r-1]) r--;
            }
        }
    }
    return nums;
};

let input1 = [2,0,1];
let input2 = [2,0,2,1,1,0];
let input3 = [0,0,0,0,0,2,1];
let input4 = [2,2,2,2,2];
let result = sortColors(input4);
console.log(result);
