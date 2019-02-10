#Given two arrays, write a function to compute their intersection.

class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        s_nums1 = set(nums1)
        s_nums2 = set(nums2)
        i_nums = s_nums1.intersection(s_nums2)
        
        temp = []

        for i in i_nums:
            n1_count = nums1.count(i)
            n2_count = nums2.count(i)
            
            if (n1_count > n2_count):
                c = n2_count
            else:
                c = n1_count
                
            for j in range(c):
                temp.append(i)
                    
        return temp
