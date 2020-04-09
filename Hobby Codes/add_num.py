# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#            self.val = x
#            self.next = None

class Solution(object):
    def print_list(self, lst):
        assert len(lst) > 0
        if len(lst) == 1:
            return ListNode(lst[0])
        else:
		    return ListNode(lst[0], self.print_list(lst[1:]))
        
     
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_val = ""
        l2_val = ""
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            l1_val += str(x)
            l2_val += str(y)
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        else:
            print("Empty List!")
        l3_sum = int(str(l1_val[::-1])) + int(str(l2_val[::-1]))
        l3_sum = str(l3_sum)
        result = self.print_list(l3_sum[::-1])
        return result
   
        
