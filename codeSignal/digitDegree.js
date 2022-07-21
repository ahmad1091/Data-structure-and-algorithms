// Let's define digit degree of some positive integer as the number of times we need to replace this number
// with the sum of its digits until we get to a one digit number.

// Given an integer, find its digit degree.

// Example

// For n = 5, the output should be
// solution(n) = 0;
// For n = 100, the output should be
// solution(n) = 1.
// 1 + 0 + 0 = 1.
// For n = 91, the output should be
// solution(n) = 2.
// 9 + 1 = 10 -> 1 + 0 = 1.
function solution(n) {
  let digits = String(n);
  if (digits.length < 2) return 0;
  let count = 0;
  for (let i = 0; i < digits.length; i++) {
    console.log(findSum(n),count);
    if (String(findSum(n)).length == 1) {
        return ++count;
    }
    n = findSum(n)
    count++;
  }
}
const findSum = (num) => {
  let sum = 0;
  while (num) {
    sum += num % 10;
    num = Math.floor(num / 10);
  }
  return sum;
};

console.log(solution(999));
// console.log(solution(123));
