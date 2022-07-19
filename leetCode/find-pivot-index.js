/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    nums[i];
    prefixSum =
      nums.slice(0, i).length > 0
        ? nums.slice(0, i).reduce((acc, e) => {
            return (acc += e);
          })
        : 0;

    suffixSum =
      nums.slice(i + 1).length > 0
        ? nums.slice(i + 1).reduce((acc, e) => {
            return (acc += e);
          })
        : 0;
    if (prefixSum == suffixSum) {
      return i;
    }
  }
  return -1;
};

console.log(pivotIndex([2, 1, -1]));
