class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        
        temp = head
        count = 0
        
        while(temp):
            count = count + 1
            temp = temp.next
            
        print(count)
        c = count - n
        
        temp = head
        
        if(c==0):
            head = temp.next
            return head
        
        if(temp.next is None):
            return None
        
        
        
        for i in range(c):
            prev = temp
            temp = temp.next
            
        prev.next = temp.next
        temp.next = None
        
        return head
        
            
        
