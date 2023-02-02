# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next

# 1. We create a dummy node and a current node to keep track of the current node we are on.
# 2. We initialize a carry variable to 0.
# 3. We loop through both lists as long as there are nodes in both lists or there is a carry.
# 4. We get the values of the current nodes in both lists. If the current node is None, we set the value to 0.
# 5. We add the values of the current nodes and the carry.
# 6. We update the carry.
# 7. We update the value of the current node.
# 8. We update the current node to the next node.
# 9. We update the current nodes in both lists.
# 10. We return the next node of the dummy node.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val  = val % 10
            cur.next = ListNode(val)

            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
