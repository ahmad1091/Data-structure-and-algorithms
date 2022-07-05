var search = function (nums, target) {
  let index = -1;
  let start = 0;
  let end = nums.length - 1;
  let middle = Math.floor((end + start) / 2);

  while (start <= end) {
    if (nums[middle] == target) return middle;
    if (nums[middle] > target) {
      end = middle - 1;
      middle = Math.floor((end + start) / 2);
    }
    if (nums[middle] < target) {
      start = middle + 1;
      middle = Math.floor((end + start) / 2);
    }
  }
  return index;
};
