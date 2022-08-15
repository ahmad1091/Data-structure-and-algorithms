// Given a string, find the number of different characters in it.

// Example

// For s = "cabca", the output should be
// solution(s) = 3.

// There are 3 different characters a, b and c.

function solution(s) {
  arr = [];
  for (e of s) {
    if (arr.indexOf(e) < 0) {
      arr.push(e);
    }
  }
  return arr.length;
}
