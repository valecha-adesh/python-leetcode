class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = set()
        temp = head
        
        if(temp is None):
                return False
            
        while(temp):
            if(temp.next in l):
                return True
            l.add(temp.next)
            temp = temp.next
            
        
        return False
            
