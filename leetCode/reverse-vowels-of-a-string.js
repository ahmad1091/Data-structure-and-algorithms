var reverseVowels = function (s) {
  const vowels = ["a", "e", "i", "o", "u"];
  splittedStr = s.split("");
  const filterVowels = splittedStr
    .filter((e) => vowels.includes(e.toLowerCase()))
    .reverse();

  return splittedStr
    .map((e) => {
      return vowels.includes(e.toLowerCase()) ? filterVowels.splice(0, 1) : e;
    })
    .join("");
};
