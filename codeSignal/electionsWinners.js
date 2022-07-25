function solution(votes, k) {
  let maxVotes = votes.reduce((acc, e) => {
    return (acc = acc > e ? acc : e);
  }, votes[0]);
  let count = votes.reduce((acc, e) => {
    return (acc += e + k > maxVotes ? 1 : 0);
  }, 0);
  let isUniqe = votes.indexOf(maxVotes) == votes.lastIndexOf(maxVotes);
  return count == 0 && isUniqe ? 1 : count;
}
