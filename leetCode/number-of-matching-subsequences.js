/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
//  "abcde", words = ["a","bb","acd","ace"]
var numMatchingSubseq = function (s, words) {
  let count = 0;
  words.map((e) => {
    let i = 0;
    let m = e.length;
    for (let j = 0; j < s.length; j++) {
      if (s[j] == e[i]) {
        i++;
      }
      if (i == m) {
        break;
      }
    }
    if (i == m) {
      count++;
    }
  });
  return count;
};
console.log(
  numMatchingSubseq("abcde", ["a","bb","acd","ace"])
);
