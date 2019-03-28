class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        summation = list(reversed(str(int(num1) + int(num2))))
        result = ListNode(0)
        temp = result
        for x in summation[:-1]:
            temp.val = int(x)
            temp.next = ListNode(0)
            temp = temp.next

        temp.val = int(summation[-1])

        return result


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end='')
        result = result.next