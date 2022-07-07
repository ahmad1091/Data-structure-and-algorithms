var rotate = function (nums, k) {
  if (nums.length < k && nums.length < 200) {
    for (let i = 0; i < k; i++) {
      nums.unshift(nums.pop());
    }
  } else {
    nums.unshift(...nums.splice(nums.length - k, k));
  }
};