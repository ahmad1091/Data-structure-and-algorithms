// "Bubble Sort" The space complexity for the algorithm is O(1)
// and the average time complexity is O(n²).
var sortArray = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
      }
    }
  }
  return nums;
};

// "Insertion Sort" The space complexity for the algorithm is O(1)
// and the average time complexity is O(n²).
var sortArray = function (nums) {
    for (let i = 0; i < nums.length; i++) {
       for (let j = i; j >= 0; j--) {
        if (nums[j]>nums[j+1]) {
            [nums[j+1],nums[j]]=[nums[j],nums[j+1]];
        }
        
       } 
    }
    return nums;
}
console.log(sortArray([5, 2, 3, 1]));
