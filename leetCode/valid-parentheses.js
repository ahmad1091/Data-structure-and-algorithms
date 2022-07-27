var isValid = function (s) {
  if(s.length <= 1) return false;
  let hash = { "(": ")", "[": "]", "{": "}" };
  let open = ["(", "{", "["];
  let occurrence = [];

  for (let i = 0; i < s.length; i++) {
    if (open.includes(s[i])) {
      occurrence.push(s[i]);
    } else if (occurrence.length > 0) {
      if (!(hash[occurrence[occurrence.length - 1]] == s[i])) {
        return false;
      } else {
        occurrence.pop();
      }
    } else {
      return false;
    }
  }
  return occurrence.length == 0;
};

console.log(isValid("())"));
