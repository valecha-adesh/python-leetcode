# Given a non-empty array of integers, every element appears twice except for one. Find that single one

##### Less Space as no new data structure is created

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        for i in nums:
            if nums.count(i) == 1:
                return i
            
##### Less Time as only checks for unique elements in set

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        for i in set(nums):
            if nums.count(i) == 1:
                return i
