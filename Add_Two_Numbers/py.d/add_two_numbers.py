import cProfile
import argparse
from arg_orchestrator import arg_func_runner
from stdout import GREEN_CHECK, RED_OCT


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def init_from_array(self, array):
        if not self.val:
           self.val = array.pop(0)
        while array:
            self += ListNode(array.pop(0))

    def traverse(self):
        temp = self
        lst_str = ''
        while temp:
            lst_str += f'{temp.val} -> '
            temp = temp.next
        print(lst_str + 'Null')

    def sum_reverse(self):
        pow = 0
        sum = 0
        temp = self
        while temp:
            sum += temp.val * (10 ** pow)
            temp = temp.next
            pow += 1
        return sum

    def __iadd__(self, other):
        """
        Overload for node1 += node2 (node1.next = node2)
        """
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = other
        return self

class Solution:
    def sum_reverse(self, listnode):
        pow = 0
        sum = 0
        temp = listnode
        while temp:
            sum += temp.val * (10 ** pow)
            temp = temp.next
            pow += 1
        return sum

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self.sum_reverse(l1) + self.sum_reverse(l2)
        new_node = ListNode()
        temp = new_node
        while sum:
            remainder = sum % 10
            sum //= 10
            temp.val = remainder
            if sum:
                temp.next = ListNode()
                temp = temp.next
        return new_node


if __name__=="__main__":
    sol = Solution()
    list1, list2 = ListNode(), ListNode()
    list1.init_from_array([2, 4, 3])
    list2.init_from_array([5, 6, 4])
    sol.addTwoNumbers(list1, list2)
