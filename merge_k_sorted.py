from functools import reduce
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """ 
        # amount = len(lists)
        # interval = 1
        # while interval < amount:
        #     for i in range(0, amount - interval, interval * 2):
        #         lists[i] = self.mergetwo(lists[i], lists[i + interval])
        #     interval *= 2
        # return lists[0] if amount > 0 else lists
        listn = len(lists)
        if not listn:
            return lists
        else:
            return self.merge_n(lists, 0, listn-1)
        
    
    def merge_n(self, lists, start, end):
        # print start, end
        if start > end:
            return None
        if start == end:
            return lists[start]
        if start == end - 1:
            return self.mergetwo(lists[start], lists[end])
        
        mid = (start + end)/2
        lowlist = self.merge_n(lists, start, mid)
        highlist = self.merge_n(lists, mid+1, end)
        
        return self.mergetwo(lowlist, highlist)
            
   
    def mergetwo(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if (l1.val <= l2.val):
            l1.next = self.mergetwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergetwo(l1, l2.next)
            return l2