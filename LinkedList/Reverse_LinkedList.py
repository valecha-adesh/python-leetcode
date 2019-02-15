class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        
        temp = head
        l = []
        while (temp):
            l.append(temp.val)
            temp = temp.next
        
        r = list(reversed(l))
        
        temp = head
    
        for i in range(len(r)):
            temp.val = r[i]
            temp = temp.next
        
        return head
    
