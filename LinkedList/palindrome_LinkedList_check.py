class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        
        temp = head
        l = []
        while (temp):
            l.append(temp.val)
            temp = temp.next
        
        r = list(reversed(l))
        
        if (r==l):
            return True
        else:
            return False
        
