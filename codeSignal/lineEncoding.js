// Given a string, return its encoding defined as follows:

// First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
// for example, "aabbbc" is divided into ["aa", "bbb", "c"]
// Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
// for example, substring "bbb" is replaced by "3b"
// Finally, all the new strings are concatenated together in the same order and a new string is returned.
// Example

// For s = "aabbbc", the output should be
// solution(s) = "2a3bc".

function solution(s) {
  let substr = 1;
  let subStrings = [];
  for (let i = 1; i < s.length; i++) {
    if (s[i] != s[i - 1]) {
      subStrings.push(substr > 1 ? substr + s[i - 1] : s[i - 1]);
      substr = 1;
    } else {
      substr++;
    }
  }
  subStrings.push(substr > 1 ? substr + s[s.length - 1] : s[s.length - 1]);
  return subStrings.join("");
}

console.log(solution("aabbbc"));
