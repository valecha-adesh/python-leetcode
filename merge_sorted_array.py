#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#Note:

#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1.remove(0)
        nums1.extend(nums2)
        nums1.sort()
