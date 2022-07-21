// Given the positions of a white bishop and a black pawn on the standard chess board,
//  determine whether the bishop can capture the pawn in one move.

// The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
// Check out the example below to see how it can move:

function solution(bishop, pawn) {
  let chessHash = { a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, g: 7, h: 8 };
  return (
    Math.abs(chessHash[bishop[0]] - chessHash[pawn[0]]) ==
    Math.abs(bishop[1] - pawn[1])
  );
}
