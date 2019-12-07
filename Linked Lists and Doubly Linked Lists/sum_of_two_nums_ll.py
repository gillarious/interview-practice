# Given two non-negative integers, represented by non-empty linked lists, 
# sum up the two numbers and return it as the properly formatted linked list.
#
# The digits of the number are stored in reverse order where each node contains a single digit.
#
# Example:
# Input: (1 -> 2 -> 3) + (4 -> 5 -> 6)
# Output: 5 -> 7 -> 9
# Explanation: 321 + 654 = 975


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode):
    n1 = ""
    while l1:
        n1 = str(l1.val) + n1
        l1 = l1.next
        
    n2 = ""
    while l2:
        n2 = str(l2.val) + n2
        l2 = l2.next
            
    res = str(int(n1) + int(n2))
    res = res[::-1]
        
    head = ListNode(int(res[0]))
    prev = head
    for i in range(1, len(res)):
        curr = ListNode(res[i])
        prev.next = curr
        prev = curr
            
    return head