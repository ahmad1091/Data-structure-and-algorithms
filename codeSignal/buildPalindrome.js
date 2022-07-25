function solution(st) {
  let arr;
  for (let i = 0; i < st.length; i++) {
    if (st == st.split("").reverse().join("")) {
      return st;
    }
    arr = st.split("");
    arr.splice(st.length - i, 0, st[i]);
    st = arr.join("");
  }
}
for (let i = 0; i < array.length; i++) {
    
}
console.log(solution("abcdc"));
