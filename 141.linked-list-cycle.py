#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head
        delay = head

        while True:
            num = 2

            for _ in range(num):
                fast = fast.next
                if fast == None:
                    return False

                if delay == fast:
                    return True

            delay = delay.next

        # @lc code=end
