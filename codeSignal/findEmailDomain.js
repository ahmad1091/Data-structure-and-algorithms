function solution(address) {
  let domain =
    address.split("@").length > 2
      ? address.split("@")[address.split("@").length - 1]
      : address.split("@")[1];
  return domain;
}

// console.log(solution("prettyandsimple@example.com"));
console.log(solution("\"very.unusual.@.unusual.com\"@usual.com"));

