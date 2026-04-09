# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        # try doing it with an array
        nav = head
        array = [] 
        while nav: # store all nodes in an array
            array.append(nav)
            nav = nav.next
        if len(array) == 1:
            return
        left, right = 0, len(array) - 1

        while left <= right:
            if left == right: # odd length approaching 
                node_next = array[left +1]
                node_next.next = array[left]
                array[left].next = None
                break
            if left+1  == right: # even length approaching
                array[right].next = None
                break
            node_next = array[left +1]
            array[left].next = array[right]
            array[right].next = node_next
            left += 1
            right -= 1