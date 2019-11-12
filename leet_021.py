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


'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

作者：LeetCode
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

