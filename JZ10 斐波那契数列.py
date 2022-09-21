# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ10 斐波那契数列.py
# @Date    : 2022/08/08:22:47
# @Author  : jinwenlong@oppo.com
class Solution:
    def Fibonacci(self, n: int) -> int:
        # write code here
        # if n < 3:
        #     return 1
        # a = 0
        # b = 1
        # for i in range(2, n + 1):
        #     b, a = a + b, b
        # return b
        # 会运行超时
        if n <= 2:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)


if __name__ == '__main__':
    print(Solution().Fibonacci(36))