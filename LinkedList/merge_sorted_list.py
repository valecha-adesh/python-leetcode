class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        
        
        temp = l1
        l_1 = []
        while (temp):
            l_1.append(temp.val)
            temp = temp.next
        
        temp = l2
        l_2 = []
        while (temp):
            l_2.append(temp.val)
            temp = temp.next
        
        l = l_1 + l_2
        s = sorted(l)
        
        print(s)

                
        if(l1 is None):
            if (l2 is None):
                return None

        
       
        if(l1 is not None):
            temp = l1
            c_temp = temp
            
            for i in range(len(l_1)):
                temp.val = s[i]
                if(temp.next is None):
                    temp.next = l2
                    break
                temp = temp.next
            
        
            temp = temp.next
        
            if(temp is None):
                return c_temp
        
        if(l2 is not None):
            if(l1 is None):
                temp = l2
                c_temp = temp

            v = len(l_1)
        
            for i in range((len(l_2))):
                temp.val = s[i + v]
            
                temp = temp.next
        
        return c_temp
        
    
