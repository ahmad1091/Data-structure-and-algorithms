//first solution with arrays build in methods
var sortedSquares = function(nums) {
    return nums.map((e)=> e**2).sort((a,b)=>a-b)
};