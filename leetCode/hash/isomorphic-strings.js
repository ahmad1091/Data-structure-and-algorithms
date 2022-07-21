/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  if (s.length !== t.length) return false;
  let firstHash = {};
  let secondHash = {};
  for (let i = 0; i < s.length; i++) {
    firstHash[s[i]] = firstHash[s[i]] ? firstHash[s[i]] + i : String(i);
    secondHash[t[i]] = secondHash[t[i]] ? secondHash[t[i]] + i : String(i);
  }
  for (let i = 0; i < s.length; i++) {
    if (firstHash[s[i]] !== secondHash[t[i]]) {
      return false;
    }
  }
  return true;
};

console.log(isIsomorphic("13", "42"));
