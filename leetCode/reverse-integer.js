var reverse = function (x) {
    let sign = x < 0 ? -1 : 1;
    let reversed = String(Math.abs(x)).split("").reverse().join('');
      if(reversed > 2**31-1 ) return 0
      return Number(reversed)* sign;
};

console.log(reverse(-123));
