# https://leetcode.com/problems/palindrome-linked-list/
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head
        if(head.next == None):
            return True
        q = head.next
        if(head.next.next):     
                r = head.next.next
                while(r.next):
                    p = p.next
                    q = q.next
                    r = r.next
                if(r.val == head.val):
                    r = head.next
                    while(q.next):
                        if(r.val == q.val):
                            q = q.next
                            r = r.next                            
                        else:
                            return False
                    if(p.val != r.val):
                        return False
                else:
                    return False
        elif(p.val != q.val):
            return False
        return True
                
