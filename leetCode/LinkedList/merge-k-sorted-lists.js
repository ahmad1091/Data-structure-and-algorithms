/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  if (lists.length == 0) return null;
  let listElements = [];
  for (let i = 0; i < lists.length; i++) {
    let nodeList = lists[i];
    while (nodeList) {
      listElements.push(nodeList.val);
      nodeList = nodeList.next;
    }
  }
  let sorted = listElements.sort((a, b) => a - b);
  let resultList = new ListNode(sorted[0]);
  let current = resultList;

  for (let i = 1; i < sorted.length; i++) {
    current.next = new ListNode(sorted[i]);
    current = current.next;
  }
  if ((resultList.val == 0) & (resultList.next == null)) return null;
  return resultList;
};
