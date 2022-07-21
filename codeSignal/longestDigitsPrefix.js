function solution(inputString) {
  let result = "";
  for (let i = 0; i < inputString.length; i++) {
    if (isNaN(inputString[i]) || inputString[i] == ' ') {
      return result;
    }
    result += inputString[i];
  }
  return result;
}

console.log(solution("  3) always check for whitespaces"));
