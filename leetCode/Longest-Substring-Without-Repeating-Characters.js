var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) {
    return s.length;
  }
  lastOccur = {};
  for (let i = 0; i < s.length; i += 2) {
    lastOccur[s[i]] = 0;
  }

  temp = s[0];
  count = 1;
  arr = [];
  for (let i = 1; i < s.length; i++) {
    if (temp.includes(s[i])) {
      arr.push(count);
      temp = s.substr(lastOccur[s[i]] + 1, i - lastOccur[s[i]]);
      count = temp.length;
      lastOccur[s[i]] = i;
    } else {
      console.log(s[i], temp);

      lastOccur[s[i]] = i;
      temp += s[i];
      count++;
    }
  }
  arr.push(count);
  console.log(arr);
  return Math.max(...arr);
};
