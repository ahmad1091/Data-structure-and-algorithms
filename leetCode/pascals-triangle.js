/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  if (numRows < 1) return [];

  let rows = [[1]];
  for (let i = 1; i < numRows; i++) {
    let row = [1, 1];
    for (let j = 1; j < i; j++) {
      row.splice(j, 0, rows[i - 1][j - 1] + rows[i - 1][j]);
    }
    rows.push(row);
    row = [];
  }
  return rows;
};

console.log(generate(5));
