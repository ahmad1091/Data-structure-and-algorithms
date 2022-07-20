/////// First Solution
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
/////// Recursive Solution
var search = function (nums, target,start = 0 , end = nums.length) {
  let middle = Math.floor((end + start) / 2);
  if (nums[middle] == target) return middle;
if (start >= end) {
  return -1
}
return target < nums[middle] ?
        search(nums,target,start,middle):
        search(nums,target,middle+1,end);

}

console.log(search([1,2,3,4,5],3))