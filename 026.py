# -*- coding: utf-8 -*-
#本题要注意的是：这道题里的循环需要用while而不是for 因为在pop删除元素之后会改变列表的长度
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0

        while i< len(nums) - 1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 0
#         while i < len(nums) - 1:
#             if nums[i] == nums[i + 1]:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return len(nums)
print Solution().removeDuplicates([1,1,2,3,3,4,4,6,6])
# nums=[1,1,2,3,3,4,4,6,6]
# print nums[2]