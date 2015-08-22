"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""
#   Since result[i] = (x1 * x2 * ... * xi-1)*(xi+1 * ... * xn)
#   So we can loop the array twice, back and forth

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        left = 1
        for i in xrange(len(nums)-1):
            left *= nums[i]
            result[i+1] *= left
        right = 1
        for i in xrange(len(nums)-1, 0, -1):
            right *= nums[i]
            result[i-1] *= right
        return result

