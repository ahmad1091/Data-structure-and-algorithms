// Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e.
// replace a with b, replace b with c, etc (z would be replaced by a).

// Example

// For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

function solution(inputString) {
  alphabet = "abcdefghijklmnopqrstuvwxyz";
  outputString = "";
  for (let index = 0; index < inputString.length; index++) {
    i =
      alphabet.indexOf(inputString[index]) == alphabet.length - 1
        ? 0
        : alphabet.indexOf(inputString[index]) + 1;
    outputString += alphabet[i];
  }
  return outputString;
}
