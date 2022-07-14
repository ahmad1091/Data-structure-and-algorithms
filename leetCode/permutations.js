/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var permute = function (nums) {
    const arr = [];
    function permutations(nums, subArr) {
      if (nums.length == 0) {
        arr.push(subArr);
      }
  
      for (let i = 0; i < nums.length; i++) {
        let n = nums[i];
        let left = nums.slice(0, i);
        let right = nums.slice(i + 1);
        let rest = left.concat(right);
        permutations(rest, subArr.concat(n));
      }
    }
    permutations(nums, []);
    return arr;
  };
  