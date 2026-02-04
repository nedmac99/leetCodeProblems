'''
You are given an array nums of lenth n. An array is trionis if there exist indices 0 < p < q < n -1 such that:
nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n - 1] is strictly increasing.
Return true if nums is trionic, otherwise return false

Example 1:
input: nums = [1,3,5,4,2,6]

output: true

Explanation:
pick p = 2, q = 4
    * nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5)
    * nums[2...4] = [5, 4, 2] is strictly descreasing (5 > 4 > 2)
    * nums[4...5] = [2, 6] is strictly increasing (2, 6)

Example 2:

'''

import pandas

nums = pandas.array()