/**
 * @param {number[][]} accounts
 * @return {number}
 */
 var maximumWealth = function(accounts) {
    let max = -Infinity;
    for(let i = 0 ; i < accounts.length ; i++){
        let totalWealth = accounts[i].reduce((acc,e)=>acc+=e);
        if(totalWealth > max){
            max = totalWealth;
        }
    }
    return max;
};

// optimize the code

var maximumWealth = function (accounts) {
    let max = -Infinity;
    for (let idx = 0; idx < accounts.length; idx++) {
      var i = 0;
      var j = accounts[idx].length - 1;
      var sum = 0;
      while (i <= j) {
        sum =
          sum + (i == j ? accounts[idx][i] : accounts[idx][i] + accounts[idx][j]);
        i++;
        j--;
      }
      if (sum > max) {
        max = sum;
      }
    }
    return max;
  };