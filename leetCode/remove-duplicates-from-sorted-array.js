/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let occurrenceArray = [];
  let k = 0;
  for (let i = 0; i < nums.length; i++) {
    if (occurrenceArray.includes(nums[i])) {
      nums[i] = Infinity;
    } else {
      occurrenceArray.push(nums[i]);
      k++;
    }
  }
  nums.sort((a, b) => a - b);

  for (let i = nums.length; i > 0; i--) {
    if (!isNaN(nums[i])) {
      break;
    }
    if (nums[i] == Infinity) {
      nums[i] = "_";
    }
  }
};

console.log(Infinity == Infinity);
