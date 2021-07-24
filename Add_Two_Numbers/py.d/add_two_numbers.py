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
           self.val = array.pop()
        while array:
            self += ListNode(array.pop())

    def traverse(self):
        temp = self
        lst_str = ''
        while temp:
            lst_str += f'{temp.val} -> '
            temp = temp.next
        print(lst_str + 'Null')

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass



if __name__=="__main__":
    sol = Solution()
    list1 = ListNode()
    list1.init_from_array([2,4,3])
    list1.traverse()
