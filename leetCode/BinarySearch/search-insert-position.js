// solution 1 with js arrays build in methods.
var searchInsert = function (nums, target) {
  if (nums.includes(target)) return nums.indexOf(target);
  if (target < nums[nums.length - 1]) {
    for (let i = 0; i < nums.length; i++) {
      if (target < nums[i]) {
        return i;
      }
    }
  }
  return nums.length - 1 + 1;
};

// solution 2 WITHOUT js arrays build in methods.
var searchInsert = function (nums, target) {
    if(target > nums[nums.length-1])return  nums.length;
    if(target < nums[0])return  0;

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


