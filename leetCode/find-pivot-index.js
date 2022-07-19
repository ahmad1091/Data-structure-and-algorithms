/**
 * @param {number[]} nums
 * @return {number}
 */
////////////brute force solution
// var pivotIndex = function (nums) {
//   for (let i = 0; i < nums.length; i++) {
//     nums[i];
//     prefixSum =
//       nums.slice(0, i).length > 0
//         ? nums.slice(0, i).reduce((acc, e) => {
//             return (acc += e);
//           })
//         : 0;

//     suffixSum =
//       nums.slice(i + 1).length > 0
//         ? nums.slice(i + 1).reduce((acc, e) => {
//             return (acc += e);
//           })
//         : 0;
//     if (prefixSum == suffixSum) {
//       return i;
//     }
//   }
//   return -1;
// };
///////////// O(n) complexity
var pivotIndex = function (nums) {
  let totalSum = nums.reduce((acc, e) => (acc += e));
  let prefixSum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (prefixSum == totalSum - nums[i]) return i;
    prefixSum += nums[i];
    totalSum -= nums[i];
  }
  return -1;
};

console.log(pivotIndex([1, 2, 3]));
