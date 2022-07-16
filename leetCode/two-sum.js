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
//////////////////////////solution with hash
var twoSum = function (nums, target) {
  let hash = {};
  for (let i = 0; i < nums.length; i++) {
    complement = target - nums[i];
    if (hash[complement] !== undefined) {
      return [hash[complement], i];
    }
    hash[nums[i]] = i;
  }
  return [];
};
console.log(twoSum([3, 2, -3], 0));
