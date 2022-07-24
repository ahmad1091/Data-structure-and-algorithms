/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let prev = null;
  let next = null;
  let current = head;
  while (current !== null) {
    next = current.next; // [2,3,4,5] // [3,4,5] // [4,5] // [5] // null
    current.next = prev; // [1,null]  // [2,1,null] // [3,2,1,null] // [4,3,2,1,null] // [5,4,3,2,1,null]
    prev = current; // [1,null]  // [2,1,null] // [3,2,1,null] // [4,3,2,4,null] // [5,4,3,2,1,null]
    current = next; // [2,3,4,5] // [3,4,5]    // [4,5] // [5] // null
  }
  return prev;
};
