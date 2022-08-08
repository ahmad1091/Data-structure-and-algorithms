// Given a rectangular matrix of characters, add a border of asterisks(*) to it.

// Example

// For

// picture = ["abc",
//            "ded"]
// the output should be

// solution(picture) = ["*****",
//                       "*abc*",
//                       "*ded*",
//                       "*****"]

function solution(picture) {
  astength = 0;
  if (picture[0]) {
    astength = picture[0].length + 2;
    border = "*".repeat(astength);
    newPicture = picture.map((ele) => {
      return "*" + ele + "*";
    });
    newPicture.push(border);
    newPicture.unshift(border);
    return newPicture;
  }
  return;
}
