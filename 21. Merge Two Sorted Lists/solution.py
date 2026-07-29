from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
    list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
    def printList(self, node):
        while node is not None:
            print(f"{node.val}", end="")
            if node.next is not None:
                print(" -> ", end="")
            node = node.next
        print()
        
if __name__ == "__main__":
    
    list1 = ListNode(5)
    list1.next = ListNode(10)
    list1.next.next = ListNode(15)
    list1.next.next.next = ListNode(40)
    
    list2 = ListNode(2)
    list2.next = ListNode(3)
    list2.next.next = ListNode(20)
    
    result = Solution().mergeTwoLists(list1, list2)
    Solution().printList(result)