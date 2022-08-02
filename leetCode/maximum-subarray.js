var maxSubArray = function(nums) {
    let maxSum = -Infinity;
    let currentSum = 0;
    for(let i = 0; i < nums.length; i++){ 
        console.log(i,'||',currentSum,'||',maxSum);
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(currentSum, maxSum);
    }
    return maxSum;
}

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
