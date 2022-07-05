// first solution with arrays build in methods
var sortedSquares = function (nums) {
  return nums.map((e) => e ** 2).sort((a, b) => a - b);
};

//secon solution WITHOUT arrays build in methods
var sortedSquares = function (nums) {
  let n = nums.length;
  let res = Array(n);
  let index = n - 1;
  let l = 0,
    r = n - 1;
  while (l <= r) {
    if (Math.abs(nums[l]) < Math.abs(nums[r])) {
      res[index--] = nums[r] * nums[r];
      r--;
    } else {
      res[index--] = nums[l] * nums[l];
      l++;
    }
  }
  return res;
};
