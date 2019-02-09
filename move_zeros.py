#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
       
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            
