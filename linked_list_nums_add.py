# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_nums_add(l1, l2):
    """
    Return the sum of the two numbers represented by l1 and l2 as a ListNode.
    The digits in l1 and l2 are stored in reverse order and each of their nodes contain a single digit.

    Ex: (2 -> 4 -> 3) is 342

    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    root = ListNode(0)
    carry_over = False
    curr = root

    while l1 or l2 or carry_over:
        v1 = v2 = 0

        if l1:
            v1 = l1.val
            l1 = l1.next

        if l2:
            v2 = l2.val
            l2 = l2.next

        curr.val = v1 + v2

        if carry_over:
            curr.val += 1
            carry_over = False
        if curr.val > 9:
            carry_over = True
            curr.val %= 10

        if l2 or l1 or carry_over:
            curr.next = ListNode(0)
            curr = curr.next

    return root


if __name__ == "__main__":
    n1 = ListNode(2)
    n1.next = ListNode(4)
    n1.next.next = ListNode(3)

    n2 = ListNode(5)
    n2.next = ListNode(6)
    n2.next.next = ListNode(4)

    result = linked_list_nums_add(n1, n2)
    while result is not None:
        print(result.val)
        result = result.next
