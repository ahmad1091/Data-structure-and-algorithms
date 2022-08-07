// A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

// The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F),
// separated by hyphens (e.g. 01-23-45-67-89-AB).

// Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

// Example

// For inputString = "00-1B-63-84-45-E6", the output should be
// solution(inputString) = true;
// For inputString = "Z1-1B-63-84-45-E6", the output should be
// solution(inputString) = false;
// For inputString = "not a MAC-48 address", the output should be
// solution(inputString) = false.

function solution(inputString) {
  let parts = inputString.split("-");
  if (parts.length < 6) return false;
  let range = [
    ...Array.from({ length: 10 }, (_, i) => i + 48),
    ...Array.from({ length: 6 }, (_, i) => i + 65),
  ];
  for (let i = 0; i < parts.length; i++) {
    let first = isNaN(parts[i]) || parts[i].charCodeAt(0);
    let second = parts[i].charCodeAt(1);
    if (!(range.includes(first) && range.includes(second))) {
      return false;
    }
  }
  return true;
}

// using regex solution
function solution(inputString) {
    let arr = inputString.split("-");
    return arr.length == 6 && arr.every((a) => /^[A-F0-9]{2}$/.test(a));
  }
  

solution("00-1B-63-84-45-E6");
