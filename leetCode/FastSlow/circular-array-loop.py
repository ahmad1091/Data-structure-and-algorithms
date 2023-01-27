# 457. Circular Array Loop

# You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
# Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

# A cycle in the array consists of a sequence of indices seq of length k where:

# Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
# Return true if there is a cycle in nums, or false otherwise.

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def nxt(arr, idx, curDir):
            nxtDir = None
            if arr[idx] >= 0:
                nxtDir = True
            else: 
                nxtDir = False

            if nxtDir != curDir or abs(arr[idx]) % len(arr) == 0: return -1

            step = idx + arr[idx]
            step = step % len(nums)

            return step

        curDir = None
        for i in range(len(nums)):
            if nums[i] >= 0:
                curDir = True
            else:
                curDir = False

            fast, slow = i, i
            while slow != fast or slow != -1 or fast != -1:
                slow = nxt(nums, slow, curDir)
                if slow == -1: break

                fast = nxt(nums, fast, curDir)
                if fast != -1:
                    fast = nxt(nums, fast, curDir)

                if fast == slow or fast == -1: break
            
            if slow == fast and slow != -1:
                return True

        return False