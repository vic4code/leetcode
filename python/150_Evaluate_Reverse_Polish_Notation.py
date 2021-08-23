#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:33:29 2021

@author: victor
"""

class Solution(object):
    def __init__(self):
        self.operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }

    def evalRPN(self, tokens):
        if not tokens:
            return 0

        stack = []

        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[0]

if __name__ == '__main__':

    tokens = ["2","1","+","3","*"]
    ans = Solution().evalRPN(tokens)
    print(ans)