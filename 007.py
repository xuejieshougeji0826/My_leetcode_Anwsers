# -*- coding: utf-8 -*-
#本题要注意的是：给定的是整形，所以需要判断是否溢出int整形的范围（-2**31——2*31-1）
#               翻转的函数是a[::-1]
class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=-x
            b=str(x)
            c=b[::-1]
            a=-1*(int(c))
            if a >= 2 ** 31 - 1:
                return 0
            elif a <= -2 ** 31:
                return 0
            else:
                return a
        else:
            b = str(x)
            c = b[::-1]
            a =(int(c))
            if a>=2**31-1:
                return 0
            elif a<=-2**31:
                return 0
            else:
                return a
#
print Solution().reverse(123)
# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         mark = 1 if x>=0 else -1
#         x_abs = abs(x)
#         result = mark * int(str(x_abs)[::-1])
#         return result if -2**31 <= result <= 2**31-1 else 0
# print Solution().reverse()