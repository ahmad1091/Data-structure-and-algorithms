/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
 var removeNthFromEnd = function (head, n) {
    let preNode = new ListNode(-Infinity);
    preNode.next = head;
    let result = preNode;
    let count = 0;
    let tail = head;
  
    while (count < n) {
      count++;
      tail = tail.next;
    }
  
    let removed = head;
    let prev = preNode;
  
    while (tail) {
      tail = tail.next;
      removed = removed.next;
      prev = prev.next;
    }
  
    prev.next = removed.next;
    result = result.next
    return result;
  };
