/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let validIndx = 0;
  for (let i = 0; i < strs[0].length; i++) {
    let valid = 1;
    for (let j = 0; j < strs.length; j++) {
      if (
        validIndx >= strs[j].length ||
        strs[j].charAt(validIndx) != strs[0].charAt(validIndx)
      ) {
        valid = 0;
        break;
      }
    }
    if (valid) {
      validIndx++;
    } else {
      break;
    }
  }
  return strs[0].slice(0, validIndx);
};

console.log(longestCommonPrefix(["dog", "flow", "flight"]));
