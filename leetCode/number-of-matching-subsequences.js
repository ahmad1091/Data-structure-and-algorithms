/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
///// Brut force solution
// var numMatchingSubseq = function (s, words) {
//   let count = 0;
//   words.map((e) => {
//     let i = 0;
//     let m = e.length;
//     for (let j = 0; j < s.length; j++) {
//       if (s[j] == e[i]) {
//         i++;
//       }
//       if (i == m) {
//         break;
//       }
//     }
//     if (i == m) {
//       count++;
//     }
//   });
//   return count;
// };
///// optimize the the solution
var numMatchingSubseq = function (s, words) {
  let count = 0;
  let charsHash = {};
  for (let i = 0; i < s.length; i++) {
    let char = [s[i]];
    charsHash[char] = charsHash[char] ? charsHash[char].concat(i) : [i];
  }
  const bs = (arr, ele) => {
    let left = 0;
    let right = arr.length;
    while (left < right) {
      let mid = Math.floor((right + left) / 2);
      if (ele < arr[mid]) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  };
  for (const subStr of words) {
    let prevIndex = -1;
    let match = true;
    for (let i = 0; i < subStr.length; i++) {
      if (charsHash[subStr[i]]) {
        let temp = bs(charsHash[subStr[i]], prevIndex);
        if (temp == charsHash[subStr[i]].length) {
          match = false;
          break;
        } else {
          prevIndex = charsHash[subStr[i]][temp];
        }
      } else {
        match = false;
        break;
      }
    }
    if (match) {
      count++;
    }
  }
  return count;
};
console.log(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]));

//////// accepted solution
const numMatchingSubseq = function (S, words) {
    const map = words.reduce((acc, word, index) => {
      const c = word[0]
      acc[c] = acc[c] || []
      acc[c].push([index, 0])
      return acc
    }, {})
    let num = 0
    for (let i = 0; i < S.length; i++) {
      if (map[S[i]] !== undefined) {
        const list = map[S[i]]
        map[S[i]] = undefined
        // eslint-disable-next-line no-loop-func
        list.forEach(([wordIndex, charIndex]) => {
          if (charIndex === words[wordIndex].length - 1) {
            num += 1
          } else {
            const nextChar = words[wordIndex][charIndex + 1]
            map[nextChar] = map[nextChar] || []
            map[nextChar].push([wordIndex, charIndex + 1])
          }
        })
      }
    }
    return num
  }
