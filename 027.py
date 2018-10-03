# -*- coding: utf-8 -*-
#本题要注意的是：删除操作直接惊醒 根据题目要求不能在占用空间，所以不能在赋值，所以直接删除
class Solution(object):
    def removeDuplicates(self,nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        while val in nums:
           nums.remove(val)
        return len(nums)
print Solution().removeDuplicates([1, 1, 2, 3, 3, 4, 4, 6, 6],1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)