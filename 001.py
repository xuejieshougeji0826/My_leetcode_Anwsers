# -*- coding: utf-8 -*-
#本题中需要注意的是，好像也没啥注意的，本答案是时间复杂度很高的暴力解法
list=[2,11,15,7,1,3,46,6,7,8,9,3,4,5,6,6,78,9,9,]
class Solution(object):
    def twoSum(self, nums, target):
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        for i in range(0,len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    print Solution().twoSum(list,18)