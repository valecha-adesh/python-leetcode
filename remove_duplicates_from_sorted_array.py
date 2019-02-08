#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        i=0
        length = len(nums) - 1
        while (i < length ):
            if(nums[i] == nums[i + 1]):
                nums.pop(i)
                i = 0
                length = length - 1
                
            else:
                i = i + 1
        return(len(nums))
