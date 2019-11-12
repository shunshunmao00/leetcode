# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        head = temp
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
                continue
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
                continue

        if l1 == None:
            temp.next = l2
        elif l2 == None:
            temp.next = l1
        return head.next


if __name__ == "__main__":
    def show(l):
        while l != None:
            print(l.val)
            l = l.next
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l = solution.mergeTwoLists(l1, l2)
    show(l)

