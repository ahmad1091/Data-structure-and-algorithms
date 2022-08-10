/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
// brut force solution
var strStr = function (haystack, needle) {
  for (let i = 0; i < haystack.length; i++) {
    let match = true;
    for (let j = 0; j < needle.length; j++) {
      if (haystack[i + j] !== needle[j]) {
        match = false;
        break;
      }
    }
    if (match) {
      return i;
    }
  }
  return -1;
};

console.log(strStr("mississippi", "issip"));
