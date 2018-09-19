# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# ZigZag Conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for _ in range(numRows)]#��¼ÿ�е�str
        row = 0
        step = 1
        for c in s:
            if row == 0:
                step = 1#ǰ��
            if row == numRows - 1:
                step = -1#����
            zigzag[row] += c
            row += step
        return ''.join(zigzag)