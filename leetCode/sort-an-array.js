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
      if (nums[j] > nums[j + 1]) {
        [nums[j + 1], nums[j]] = [nums[j], nums[j + 1]];
      }
    }
  }
  return nums;
};

// "Selection Sort" The space complexity for the algorithm is O(1)
// and the average time complexity is O(n²).
var sortArray = function (nums) {
  let min;
  for (let i = 0; i < nums.length; i++) {
    min = i;
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] < nums[min]) {
        min = j;
      }
    }
    if (min !== i) {
      [nums[i], nums[min]] = [nums[min], nums[i]];
    }
  }
  return nums;
};

// "Merge Sort" The space complexity varies depending on the technique.
// and the average time complexity is O(n * log n).
var merge = function (arr1, arr2) {
  let result = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
};

var sortArray = function (nums) {
  if (nums.length <= 1) return nums;

  let mid = Math.floor(nums.length / 2);
  let left = sortArray(nums.slice(0, mid));
  let right = sortArray(nums.slice(mid));

  return merge(left, right);
};

// "Quick Sort" The space complexity varies depending on the technique.
// and the average time complexity is O(n * log n).
var partition = function (arr, start = 0, end = arr.length - 1) {
  let pivot = arr[start];
  let pivotIdx = start;

  for (let i = start+1; i <= end; i++) {
    if (arr[i] < pivot) {
      pivotIdx++;
      [arr[i], arr[pivotIdx]] = [arr[pivotIdx], arr[i]];
    }
  }
  [arr[pivotIdx], arr[start]] = [arr[start], arr[pivotIdx]];
  return pivotIdx;
};

var sortArray = function (nums,left = 0 , right=nums.length-1) {

    if (left<right) {
        let pivotIndex = partition(nums,left,right);

        sortArray(nums,left,pivotIndex-1);
        sortArray(nums,pivotIndex+1,right);
    }
    return nums;
}
console.log(partition([5,3, 2, 1]));
