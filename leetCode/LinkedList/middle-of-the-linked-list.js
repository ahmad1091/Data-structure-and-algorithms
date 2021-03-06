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
var middleNode = function (head) {
  let size = 0;
  let node = head;
  while (node) {
    size++;
    node = node.next;
  }

  steps = Math.floor(size / 2);
  while (steps > 0) {
    head = head.next;
    steps--;
  }
  return head;
};

/// another solution

var middleNode = function (head) {
  var count = 0;
  var mid = head;

  while (head != null) {
    if (count % 2 == 1) mid = mid.next;
    ++count;
    head = head.next;
  }
  return mid;
};
