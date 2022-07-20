var search = function (nums, target) {
  let start = 0;
  let end = nums.length;
  while (start < end) {
    let middle = Math.floor((end + start) / 2);
    if (nums[middle] == target) return middle;
    if (target<nums[middle]) {
      end = middle;
    } else{
      start = middle + 1;
    }
  }
  return -1;
};

console.log(search([1,2,3,4,5],4))