/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

// solution using built in methods
var findMedianSortedArrays = function (nums1, nums2) {
  sortedMerged = nums1.concat(nums2).sort((a, b) => a - b);
  if (sortedMerged.length % 2 == 0) {
    firstHalf = Math.floor(sortedMerged.length / 2) - 1;
    secondHalf = Math.floor(sortedMerged.length / 2);
    return (sortedMerged[firstHalf] + sortedMerged[secondHalf]) / 2;
  } else {
    half = Math.floor(sortedMerged.length / 2);
    return sortedMerged[half];
  }
};

console.log(findMedianSortedArrays([1, 2], [3, 4]));
