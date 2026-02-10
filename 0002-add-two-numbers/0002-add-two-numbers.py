# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        Dummy_Node = ListNode(0)
        current = Dummy_Node
        carry = 0
        while (l1 is not None or l2 is not None or carry > 0):
            if (l1 is not None):
                v1 = l1.val
            else:
                v1 = 0
            if (l2 is not None):
                v2 = l2.val
            else:
                v2 = 0
            soma_total = v1 + v2 + carry
            carry = soma_total // 10
            digito = soma_total % 10
            current.next = ListNode(digito)
            current = current.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        return Dummy_Node.next
                