var moveZeroes = function (nums) {
  temp = [...nums];
  end = temp.length - 1;
  start = 0;
  for (let i = 0; i < temp.length; i++) {
    if (temp[i] === 0) {
      nums[end--] = temp[i];
    } else {
      nums[start++] = temp[i];
    }
  }
};
