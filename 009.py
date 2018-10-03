# -*- coding: utf-8 -*-
#本题需要注意的是
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=int(str(x)[::-1])
        if x<0:
            return False

        elif x!=y:
            return False
        else:
            return True

print Solution().isPalindrome(1212222221)
# class Solution:
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
#         elif x != int(str(x)[::-1]):
#             return False
#         else:
#             return True
# print Solution().isPalindrome(121)