/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  if (nums.length <= 1) return null;
  if (nums.length == 2) return nums[0] + nums[1] == target ? [0, 1] : null;

  for (let i = 0; i < nums.length; i++) {
    if (nums.includes(target - nums[i])) {
      let first = i;
      let second = nums.lastIndexOf(target - nums[i]);
      if (first !== second) {
        return [first, second];
      }
    }
  }
  return null;
};

console.log(twoSum([3, 2, -3], 0));
