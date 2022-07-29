/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  let i = 0;
  while (true) {
    if (nums[i] == undefined) break;
    if (nums[i] == val) {
      nums.splice(i, 1);
    } else {
      i++;
    }
  }
  console.log(nums);
};

removeElement([3,2,2,3], 2);
