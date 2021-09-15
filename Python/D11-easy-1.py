#!/usr/bin/python


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        the idea is credited to leetcode user Nathan_Fegard
        """
        for index, single in enumerate(nums):
            wanted = target - single
            try:
                res = [i for i,d in enumerate(nums) if d==wanted]
                if res[0] == index:
                    return [index, res[1]]
                else:
                    return [index, res[0]]
            except:
                continue

a = Solution.twoSum(Solution, [3,3], 6)
print(a)

"""
Another solution: Credit to leetcode user __guoqiao__
"""

def twoSum(self, nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i
