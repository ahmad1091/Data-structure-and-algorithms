/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
 var checkInclusion = function (s1, s2) {
    if (s1.length > s2.length || s2.length == 0) return false;
    if (s1.length == 0) return true;
    let firstLen = s1.length;
    let secondLen = s2.length;
  
    arr1 = Array(26).fill(0);
    arr2 = Array(26).fill(0);
  
    for (let i = 0; i < firstLen; i++) {
      arr1[s1.charCodeAt(i) - 97]++;
      arr2[s2.charCodeAt(i) - 97]++;
    }
  
    for (let i = firstLen; i < secondLen; i++) {
      if (String(arr1) == String(arr2)) return true;
      arr2[s2.charCodeAt(i - firstLen) - 97]--;
      arr2[s2.charCodeAt(i) - 97]++;
    }
    if (String(arr1) == String(arr2)) return true;
    return false;
  };
  
  
  
  