function solution(inputString) {
  let alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  let alphabetIndices = {};
  for (let i = 0; i < alphabet.length; i++) {
    alphabetIndices[alphabet[i]] = 0;
  }

  for (let i = 0; i < inputString.length; i++) {
    alphabetIndices[inputString[i]]++;
  }
  let a = Object.values(alphabetIndices);
  return String(a) == String([...a].sort((a, b) => b - a));
}

console.log(solution("bbbaacdafe"));
