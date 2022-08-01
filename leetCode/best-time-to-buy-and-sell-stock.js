/**
 * @param {number[]} prices
 * @return {number}
 */

// brut force solution
var maxProfit = function (prices) {
  let sell = [...prices.slice(1)].sort((a, b) => a - b);
  let buy = [...prices.slice(0, prices.length - 1)].sort((a, b) => b - a);
  console.log("Buy", buy);
  console.log("sell", sell);
  let max = -Infinity;
  for (let i = 0; i < buy.length; i++) {
    for (let j = 0; j < sell.length; j++) {
      if (
        sell[j] - buy[i] > max &&
        prices.indexOf(buy[i]) < prices.lastIndexOf(sell[j])
      ) {
        max = sell[j] - buy[i];
      }
    }
  }
  return max < 0 ? 0 : max;
};

console.log(maxProfit([2,1,2,0,1]));
